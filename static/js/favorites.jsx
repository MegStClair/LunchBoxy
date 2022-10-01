//////////////////////// DISPLAY ALL FAVORITES ///////////////////////////////////////

function ShowFavoriteComponent(props) {
    console.log("jdbkfjfhlflkglkglgk")
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
        .then((data) => {setFavorites(data)})
        }, [])

    const userFavorites = [];
    console.log(favorites)
    for (const currentFavorite of favorites) {
        userFavorites.push(
            
            <ShowFavoriteComponent
                title={currentFavorite.recipe.title}
                image={currentFavorite.image}
                ingredients={currentFavorite.ingredients}
                instructions={currentFavorite.instructions}
                tips={currentFavorite.tips}
                
            />
        );
    }
    console.log(userFavorites)
    return (
        <div className="grid">{userFavorites}</div>
    );

    }

    ReactDOM.render(<AllFavoritesContainer />, document.getElementById('container'));
