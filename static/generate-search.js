

document.querySelector('#restrictions').querySelector('button').addEventListener('click', (evt) => {
    evt.preventDefault();

    const formInputs = {
    diet: document.querySelector('#diet').value,
    exclude: document.querySelector('#exclude').value,
    intolerances: document.querySelector('#intolerances').value,
    maxReady: document.querySelector('#max-ready-time').value
    };
    
    // const showResults = evt.target.querySelector('input').value;
    fetch('/api/search-results', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
          'Content-Type': 'application/json',
        }}).then((response) => 
        response.json()

    ).then((data) => { 
        for (const item of data['results']) {
            document.querySelector('#search-results').append('beforeend', item['title'])
        }
        // document.querySelector('#search-results').innerHTML = data['results'];
    })


    }
)