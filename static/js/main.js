const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const btnAray = Array.from(btnDelete);
    btnAray.forEach((btn)=>{
        btn.addEventListener('click',(e) =>{
            if (!confirm('Estas seguro de eliminar este cliente?')) {
                e.preventDefault();
            }
        })
    })
}