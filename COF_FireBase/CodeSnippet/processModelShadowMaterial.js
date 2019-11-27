//function update( event ) {}
this.traverse((child)=>{
    child.castShadow = true;
    child.receiveShadow = true;
    if (child.isMesh){
        shadow(child);
    }
});
console.log(this);
function shadow(child){
    var oldcolor = new THREE.Color();
    oldcolor = child.material.color;
    var newMaterial = new THREE.MeshPhysicalMaterial()
    newMaterial.color.set(oldcolor);
    child.material = newMaterial;
    console.log(child.material);
}