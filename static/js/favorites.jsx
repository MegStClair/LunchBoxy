// DISPLAY ALL FAVORITES 

function ShowFavoriteComponent(props) {
    return(
        <div id="favorite">
            <h2>{ props.title }</h2>
            <img src={ props.image } width={300}/> 
            </div>
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
            
            <ShowFavoriteComponent
                title={currentFavorite.recipe.title}
                image={currentFavorite.recipe.image}
                ingredients={currentFavorite.recipe.ingredients}
                instructions={currentFavorite.recipe.instructions}
                tips={currentFavorite.recipe.tips}  
            />
        );
    }
    
    console.log(userFavorites)
    return (
        <div className="grid">{userFavorites}</div>
    );

    }

    ReactDOM.render(<AllFavoritesContainer />, document.getElementById('container'));
