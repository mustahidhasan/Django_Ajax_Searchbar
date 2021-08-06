const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultBox = document.getElementById('result-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (uniName) =>{
    $.ajax({
        type : 'POST',
        url : 'search/',
        data :{
            'csrfmiddlewaretoken' : csrf,
            'uniName' : uniName
        },
        success :(res)=>{
            console.log(res.data)
            const data = res.data
            resultBox.innerHTML =""
            if(Array.isArray(data)){
                data.forEach(uniName=>{
                    resultBox.innerHTML +=`
                    <a href ="${uniName.url}" class ="item">
                    <div class="row">
                        <div class ="col-12">
                        <h5>${uniName.name}
                        </div>
                    </div>
                    `
                })


            }else{
                if(searchInput.value.length > 0){
                    resultBox.innerHTML = `<b>${data}</b>`
                }else{
                    resultBox.classList.add('not_visible')
                }
            }
        },
        error: (err)=>{
            console.log(err)
        }


    })
}
searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)
    if(resultBox.classList.contains('not_visible')){
        resultBox.classList.remove('not_visible')
    }
    sendSearchData(e.target.value)
})