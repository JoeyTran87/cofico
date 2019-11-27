function update( event ) {
	var time = event.time * 0.0003;
	this.position.x = Math.sin( time ) * 2;
	this.position.z = Math.cos( time ) * 2;
	this.lookAt( scene.position );
}