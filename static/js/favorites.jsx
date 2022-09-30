
function FavoritesComponent(props) {
    return (
        <div id="favorite">
            <h2>{ props.title }</h2>
            <img src={ props.image } width={500}/>
        
        </div>
    );
}

function FavoritesContainer(props) {
    return (
        <div id="all-favorites">
            <FavoritesComponent { ...props}/>
        </div>
    )
}

fetch('/favorites.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<FavoritesContainer {...recipes}/>, document.getElementById('container'));

});