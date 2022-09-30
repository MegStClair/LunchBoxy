

// allow user to favorite/unfavorite recipes 
class FavoriteButton extends React.Component {
    constructor() {
        super();
        this.state = { value:heartEmpty };
        
        this.addFavorite = this.addFavorite.bind(this);
        this.notLoggedIn = this.notLoggedIn.bind(this);
        this.favorited = this.favorited.bind(this);

    }

    //  set heart to filled if already in user's favs
    componentDidMount() {
        if (userID !== "None") {
            fetch('/favorite-status')
            .then (response => response.json())
            .then (data => {
                if (data === true) {
                    this.setState({ value: heartFilled });
                }
            })
        }

    }

    // handle favorite button click
    addToFavorites() {
        if (userID !== "None") {
            $.post("/update-favorites",
                {"recipe_id": recipeID}, this.favorited);
        } else {
            this.notLoggedIn();
        }
    }

    // update heart when favorited/unfavorited
    favorited(result) {
        if (result === "Favorite added") {
            this.setState({ value: heartFilled });
        } else {
            this.setState({ value: heartEmpty });
        }
    }

    render() {
        return (
            <span className={this.state.value} onClick={this.addFavorite}></span>
        );
    }
}


// GET USER ID & RECIPE ID HTML ATTRIBUTES??? 
// const userID = querySelector.....??
// const recipeID = querySelector.....??


// INSERT HEART ICONS???
// let heartEmpty = '???';
// let heartFilled = '????';


// ReactDOM.render(
//     <FavoriteButton />, document.getElementById('')
// );





//////////////////////// DISPLAY ALL FAVORITES ///////////////////////////////////////


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