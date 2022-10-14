// DISPLAY ALL FAVORITES 

function ShowFavoriteComponent(props) {
    return(
        <div id="favorite">
            <h2>{ props.title }</h2>
            <img src={ props.image } width={300}/> 
            </div>
    );   
}


function RemoveButtonComponent(props) {
    
    function removeFromFavorites(evt) {
        console.log('button clicked')
        evt.preventDefault();

        const removeButton = evt.target;
            
            const favRecipe = {
                favorite_id: props.favoriteId
            }
            // console.log(favRecipe);
            // console.log(evt.target);
                fetch('/remove-from-favorites', {
                    method: 'POST',
                    body: JSON.stringify(favRecipe),
                    headers: {
                        'Content-Type': 'application/json',
                      },
                })
                .then((response) => response.json())
                .then((data) => console.log(data));
            const initialText = "REMOVE FROM FAVORITES"
    
            if (removeButton.innerHTML == initialText) {
                removeButton.innerHTML = "REMOVED!";
            } else {
                removeButton.innerHTML = initialText;
            }
        }

    return (
        <button id="remove-button" 
            favorite_id={ props.favoriteId } 
            onClick={ removeFromFavorites }>REMOVE FROM FAVORITES</button>
    );
}


function AllFavoritesContainer() {

    const [favorites, setFavorites] = React.useState([]);

    React.useEffect(() => {
        fetch('/favorites.json')
        .then((response) => response.json())
        .then((data) => {setFavorites(data)
            console.log("data.favorites=", data)})
        }, [])

    const userFavorites = [];

    for (const currentFavorite of favorites) {
        userFavorites.push(
            <div id="remove">
            <ShowFavoriteComponent
                favorite_id={currentFavorite.favorite_id}
                recipeId={currentFavorite.recipe_id}
                title={currentFavorite.recipe.title}
                image={currentFavorite.recipe.image}
                ingredients={currentFavorite.recipe.ingredients}
                instructions={currentFavorite.recipe.instructions}
                tips={currentFavorite.recipe.tips}  
            />
            <RemoveButtonComponent
                favoriteId={currentFavorite.favorite_id}
            />
            </div>
        );
    }
    
    console.log(userFavorites)
    return (
        <div id="favs-container">
            <div id="something" className="row-md-12 text-center"></div>
            <div className="grid">{userFavorites}</div>
        </div>
        
    );

    }

    ReactDOM.render(<AllFavoritesContainer />, document.getElementById('container'));