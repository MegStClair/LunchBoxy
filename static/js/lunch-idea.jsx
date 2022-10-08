// SHOW LUNCH IDEA

function FillingComponent(props) {
    // props: recipe_id, tag, title, ingredients, instructions, tip    
    return (
        <div id="filling">
        <h1>{ props.title }</h1>
        <img id="filling-img" src={ props.image } width={500}/>
        <p> <b>Ingredients: </b> { props.ingredients }</p>
        <p> <b>Directions: </b>{ props.instructions }</p>
    
        <p><b>Tip!</b> { props.tips }</p>
        </div>
    );
    }


function FavoriteButtonComponent(props) {

    function addToFavorites(evt) {
        evt.preventDefault();

        const favButton = document.querySelector('#fav-button');
            
            const favRecipe = {
                recipe_id: props.recipeId
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
            
        
            const initialText = "ADD TO FAVORITES"
        
            if (favButton.innerHTML == initialText) {
            favButton.innerHTML = "FAVORITED!";
            } else {
                favButton.innerHTML = initalText;
            }
    }

    return (
        <button id="fav-button" 
            recipe_id={ props.recipeId }
            onClick={ addToFavorites }>ADD TO FAVORITES</button>

    );
}    



function SidesComponent(props) {

        return (
            <div id="sides">
            <h2>{ props.title }</h2>
            <img className="img" src={ props.image } width={200}/>
            </div>
        );
    }



function RecipeContainer(props) {

    return (
        <div id="recipe-container">
            <div id="filling">
            <FillingComponent {...props.filling}/>
            <FavoriteButtonComponent
                recipeId={props.filling.recipe_id}/>
            </div><br/><br/>

            <div id="crunchy">
            <SidesComponent {...props.crunchy}/>
            </div><br/><br/>

            <div id="fresh">
            <SidesComponent {...props.fresh}/>
            </div><br/><br/>

        </div>    
    )
}

fetch('/lunch-idea.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<RecipeContainer {...recipes}/>, document.getElementById('container'));

})