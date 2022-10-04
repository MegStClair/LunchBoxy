// SHOW LUNCH IDEA

function FillingComponent(props) {
    // props: recipe_id, tag, title, ingredients, instructions, tips
    
    function addToFavorites(evt) {
        console.log('button clicked')
        evt.preventDefault();

        const favButton = document.querySelector('#fav-button');
            
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
            <br/><br/>
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