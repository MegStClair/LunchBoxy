// SHOW LUNCH IDEA

function FillingComponent(props) {
    // props: recipe_id, tag, title, ingredients, instructions, tip    
    return (
        <div className="row">
            <div id="leftcolumn" className="col-md-6">
                <img id="filling-img" src={ props.recipe.image } className="rounded mx-auto d-block"/>
            </div>

            <div id="rightcolumn" className="col-md-6 text-center">
            <h1>{ props.recipe.title }</h1>
            
            <p> <b>Ingredients: </b> { props.recipe.ingredients }</p>
            <p> <b>Directions: </b>{ props.recipe.instructions }</p>
        
            <p><b>Tip!</b> { props.recipe.tips }</p>
            
            <FavoriteButtonComponent
                recipeId={props.recipe.recipe_id}/>
            </div>
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
                favButton.innerHTML = initialText;
            }
    }

    return (
        
        <button id="fav-button" className="btn btn-success btn-block"
            recipe_id={ props.recipeId }
            onClick={ addToFavorites }>ADD TO FAVORITES</button>
    );
}    



function SidesComponent(props) {

        return (
            <div id="bottom" className="row">
                <h2>{ props.recipe.title }</h2>
                <img src={ props.recipe.image } className="rounded mx-auto d-block"/>
            </div>
        );
    }



function RecipeContainer(props) {
console.log(props.recipes)
    return (
        
        <div id="recipe-container" >
            <div id="top" className="row-md-12 text-center">Let's pack a lunch with:</div>
            <div id="something" className="row-md-12 text-center">SOMETHING FILLING</div>
            <div id="filling" className="row">
            <FillingComponent recipe={props.recipes.filling}/>
            </div>
            <div id="something" className="row">
                <div className="col-md-4 text-center">SOMETHING CRUNCHY</div>
                <div className="col-md-8 text-center">SOMETHING FRESH</div>
            </div>
            <div id="sides" className="row">
            <div className="col-md-4"><SidesComponent recipe={props.recipes.crunchy}/></div>
            <div className="col-md-4"><SidesComponent recipe={props.recipes.fresh}/></div>
            <div className="col-md-4"><SidesComponent recipe={props.recipes.fresh2}/></div>
            </div>

        </div>    
    )
}

fetch('/lunch-idea.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<RecipeContainer recipes={recipes}/>, document.getElementById('container'));

})