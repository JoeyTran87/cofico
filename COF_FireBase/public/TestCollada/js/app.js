/**
 * @author mrdoob / http://mrdoob.com/
 */

// tvpduy editting 191121


var APP = {

	Player: function () {

		//tvpduy editing 191121
		var cameraStop = new THREE.PerspectiveCamera(45,1920/1080,1,2000);//(fov,aspect,near,far)
		var jsonCamera;
		var camposx=camposy=camposz=0;
		var countSpace = 0;

		var loader = new THREE.ObjectLoader();
		var camera, scene, renderer;

		var events = {};

		var dom = document.createElement( 'div' );

		this.dom = dom;

		this.width = 500;
		this.height = 500;

		

		this.load = function ( json ) {

			renderer = new THREE.WebGLRenderer( { antialias: true } );
			renderer.gammaOutput = true;
			renderer.setClearColor( 0x000000 );
			renderer.setPixelRatio( window.devicePixelRatio );

			var project = json.project;

			if ( project.shadows ) renderer.shadowMap.enabled = true;
			if ( project.vr ) renderer.vr.enabled = true;

			dom.appendChild( renderer.domElement );

			this.setScene( loader.parse( json.scene ) );
			this.setCamera( loader.parse( json.camera ) );

			events = {
				init: [],
				start: [],
				stop: [],
				keydown: [],
				keyup: [],
				mousedown: [],
				mouseup: [],
				mousemove: [],
				touchstart: [],
				touchend: [],
				touchmove: [],
				update: []
			};

			var scriptWrapParams = 'player,renderer,scene,camera';
			var scriptWrapResultObj = {};

			for ( var eventKey in events ) {

				scriptWrapParams += ',' + eventKey;
				scriptWrapResultObj[ eventKey ] = eventKey;

			}

			var scriptWrapResult = JSON.stringify( scriptWrapResultObj ).replace( /\"/g, '' );

			for ( var uuid in json.scripts ) {

				var object = scene.getObjectByProperty( 'uuid', uuid, true );

				if ( object === undefined ) {

					console.warn( 'APP.Player: Script without object.', uuid );
					continue;

				}

				var scripts = json.scripts[ uuid ];

				for ( var i = 0; i < scripts.length; i ++ ) {

					var script = scripts[ i ];

					var functions = ( new Function( scriptWrapParams, script.source + '\nreturn ' + scriptWrapResult + ';' ).bind( object ) )( this, renderer, scene, camera );

					for ( var name in functions ) {

						if ( functions[ name ] === undefined ) continue;

						if ( events[ name ] === undefined ) {

							console.warn( 'APP.Player: Event type not supported (', name, ')' );
							continue;

						}

						events[ name ].push( functions[ name ].bind( object ) );

					}

				}

			}

			dispatch( events.init, arguments );

		};

		this.setCamera = function ( value ) {
			
			jsonCamera = value;
			
			var newcamera = value;
			camera = newcamera.clone();

			camera.aspect = this.width / this.height;
			camera.updateProjectionMatrix();

			if ( renderer.vr.enabled ) {
				dom.appendChild( THREE.WEBVR.createButton( renderer ) );
			}

			var group = new THREE.Group();
			group.add( camera );
			scene.add( group );
		};
		function orbitAnimate(obj) {
			var time = event.time * 0.0003;
			this.position.x = Math.sin( time ) * 2;
			this.position.z = Math.cos( time ) * 2;
			this.lookAt( scene.position );
		}

		this.setScene = function ( value ) {

			scene = value;
			// tvpduy editting 191121
			this.scene = scene;

		};

		this.setSize = function ( width, height ) {

			this.width = width;
			this.height = height;

			if ( camera ) {

				camera.aspect = this.width / this.height;
				camera.updateProjectionMatrix();

			}

			if ( renderer ) {

				renderer.setSize( width, height );

			}

		};

		function dispatch( array, event ) {

			for ( var i = 0, l = array.length; i < l; i ++ ) {

				array[ i ]( event );

			}

		}

		var time;
		var prevTime;
		var timedelta = 0;
		//
		function onDocumentKeyDown( event ) {

			dispatch( events.keydown, event );
		}

		function onDocumentKeyDownStop( event ) {

			dispatch( events.keydown, event );
			
			var keyCode = event.which;
			if (keyCode == 32) {
				camera = cameraStop;
			}
			
		}
		function onDocumentKeyDownRestart( event ) {

			dispatch( events.keydown, event );
			
			var keyCode = event.which;
			if (keyCode == 192) {
				camera = jsonCamera;
			}
		}

		function animate() {

			time = performance.now();

			timedelta = time - prevTime;

			//cameraStop = camera.clone();

			if (camera.parent != null){
				camposx = camera.position.x + camera.parent.position.x;
				camposy = camera.position.y + camera.parent.position.y;
				camposz = camera.position.z + camera.parent.position.z;

				cameraStop.position.x = camposx;
				cameraStop.position.y = camposy;
				cameraStop.position.z = camposz;
			}		
			cameraStop.fov = camera.fov;
			cameraStop.aspect = camera.aspect;			
			cameraStop.near = camera.near;
			cameraStop.far = camera.far;

			try {
				dispatch( events.update, { time: time, delta: timedelta } );
			} catch ( e ) {
				console.error( ( e.message || e ), ( e.stack || "" ) );
			}
			prevTime = time;
			renderer.render(scene, camera);
		}

		this.play = function () {

			prevTime = performance.now();
			dispatch( events.start, arguments );
						
			document.addEventListener( 'keydown', onDocumentKeyDown );
			document.addEventListener( 'keydown', onDocumentKeyDownStop );
			document.addEventListener( 'keydown', onDocumentKeyDownRestart );
			document.addEventListener( 'keyup', onDocumentKeyUp );
			//
			document.addEventListener( 'mousedown', onDocumentMouseDown );
			document.addEventListener( 'mouseup', onDocumentMouseUp );
			//
			document.addEventListener( 'mousemove', onDocumentMouseMove );
			document.addEventListener( 'touchstart', onDocumentTouchStart );
			document.addEventListener( 'touchend', onDocumentTouchEnd );
			document.addEventListener( 'touchmove', onDocumentTouchMove );

			renderer.setAnimationLoop( animate);
			

		};

		this.stop = function () {

			document.removeEventListener( 'keydown', onDocumentKeyDown );
			document.removeEventListener( 'keyup', onDocumentKeyUp );
			document.removeEventListener( 'mousedown', onDocumentMouseDown );
			document.removeEventListener( 'mouseup', onDocumentMouseUp );
			document.removeEventListener( 'mousemove', onDocumentMouseMove );
			document.removeEventListener( 'touchstart', onDocumentTouchStart );
			document.removeEventListener( 'touchend', onDocumentTouchEnd );
			document.removeEventListener( 'touchmove', onDocumentTouchMove );

			dispatch( events.stop, arguments );

			renderer.setAnimationLoop( null );

		};

		this.dispose = function () {

			while ( dom.children.length ) {

				dom.removeChild( dom.firstChild );

			}

			renderer.dispose();

			camera = undefined;
			scene = undefined;
			renderer = undefined;

		};

		

		function onDocumentKeyUp( event ) {

			dispatch( events.keyup, event );

		}

		function onDocumentMouseDown( event ) {

			dispatch( events.mousedown, event );

			
		}

		function onDocumentMouseUp( event ) {

			dispatch( events.mouseup, event );

			//tvpduy editting 191121
			//camera = jsonCamera;

		}

		function onDocumentMouseMove( event ) {

			dispatch( events.mousemove, event );

		}

		function onDocumentTouchStart( event ) {

			dispatch( events.touchstart, event );

		}

		function onDocumentTouchEnd( event ) {

			dispatch( events.touchend, event );

		}

		function onDocumentTouchMove( event ) {

			dispatch( events.touchmove, event );

		}

	}

};
