var firebaseConfig = {
    apiKey: "AIzaSyBaYDvLN3W6s82UJvdDc_pGfIsYN1HDf-g",
    authDomain: "cofico-a4176.firebaseapp.com",
    databaseURL: "https://cofico-a4176.firebaseio.com",
    projectId: "cofico-a4176",
    storageBucket: "cofico-a4176.appspot.com",
    messagingSenderId: "736228987092",
    appId: "1:736228987092:web:5a4556064f4773b391ab41",
    measurementId: "G-08NKC17ZJL"
  }
  firebase.initializeApp(firebaseConfig)

  var uploader = document.getElementById('uploader')
  var fileButton = document.getElementById('fileButton')

  fileButton.addEventListener('change',function(e){
    for(let i = 0; i<e.target.files.length; i++){
        var file = e.target.files[i]
        var storageRef = firebase.storage().ref('testUpload/' + file.name)
        var task = storageRef.put(file)
        task.on('state_changed',function progress(snapshot){
            var percentage = (snapshot.bytesTransferred / snapshot.totalBytes )*100
            console.log(percentage + "% Done")
            uploader.value = percentage
            },
            function error (err) {
      
            },
            function complete(){
      
            })
    }
    
    /* case: single file
    var file = e.target.files[0]
    var storageRef = firebase.storage().ref('testUpload/' + file.name)
    var task = storageRef.put(file)
    //progress bar
    
    task.on('state_changed',function progress(snapshot){
      var percentage = (snapshot.bytesTransferred / snapshot.totalBytes )*100
      //console.log(snapshot.bytesTransferred)
      //console.log(snapshot.totalBytes)
      console.log(percentage + "% Done")
      uploader.value = percentage
      },
      function error (err) {

      },
      function complete(){

      })
      */

  })