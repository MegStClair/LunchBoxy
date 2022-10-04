// props = title, image, ingredients, instructions, tips

function FillingComponent(props) {

    // define callback for click event here 
    function addToFavorites(evt) {
        console.log('button clicked')
        evt.preventDefault();

        const favButton = document.querySelector('#fav-button');

        // favButton.addEventListener('click', (evt) => {
            
            const favRecipe = {
                recipe_id: evt.target.dataset.recipeId

            }

                fetch('/add-to-favorites', {
                    method: 'POST',
                    body: JSON.stringify(favRecipe),
                    headers: {
                        'Content-Type': 'application/json',
                      },
                })
                .then((response) => response.json())
                .then((data) => console.log(data));

        }
    

    return (
        <div id="filling">
        <h1>{ props.title }</h1>
        <img src={ props.image } width={500}/>
        <p> <b>Ingredients: </b> { props.ingredients }</p>
        <p> <b>Directions: </b>{ props.instructions }</p>
    
        <p><b>Tip!</b> { props.tips }</p>
        <button id="fav-button" data-recipe-id={ props.recipe_id } onClick={ addToFavorites }>ADD TO FAVORITES</button>
        </div>
    );
    }


    // inside component where button should be, add a button, it will have onClick attribute = function to call when button is clicked 
    //(insdie body of function make fetch req.)
    // either send id of recipe as part of body (AJAX lecture) or part of URL /fav/${rec_id}

function SidesComponent(props) {
        return (
            <div id="sides">
            <h2>{ props.title }</h2>
            <img src={ props.image } width={200}/>
            </div>
        );
        }


function RecipeContainer(props) {
    return (
        <div id="lunch">
        <FillingComponent {...props.filling}/>
            
            <div id="crunchy">
            <SidesComponent {...props.crunchy}/>
            </div>
    
            <div id="fresh">
            <SidesComponent {...props.fresh}/>
            </div>

            <div id="fresh2">
            <SidesComponent {...props.fresh2}/>
            </div>

        </div>
    
    )
}

fetch('/lunch-idea.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<RecipeContainer {...recipes}/>, document.getElementById('container'));

})