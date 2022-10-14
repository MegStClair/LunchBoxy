// DISPLAY ALL MEALS 

function ShowMealComponent(props) {

    const [showDetails, setShowDetails] = React.useState(false)

    function handleShowDetails() {

        setShowDetails (!showDetails) 
        
    }
    let details = null 
    if (showDetails===true) {
        details = (
        <div className="details">
        <p><b>Ingredients: </b> { props.ingredients }</p>
        <p><b>Directions: </b>{ props.instructions }</p>
    
        <p><b>Tip!</b> { props.tips }</p>
        </div>)
    }

    return (
        <div className="meal">
        <h2>{ props.title }</h2>
        <img 
            src={ props.image } 
            width={300} 
            onClick={handleShowDetails}
        />

            <div>{ details }</div>
        </div>
        
    );

}

function FavoriteButtonComponent(props) {
    
    function addToFavorites(evt) {
        evt.preventDefault();

        const favButton = evt.target;
            
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
        <button id="fav-button" 
            recipe_id={ props.recipeId } 
            onClick={ addToFavorites }>ADD TO FAVORITES</button>

    );
}


function MealContainer() {

    const [meals, setMeals] = React.useState([]);

    React.useEffect(() => {
        fetch('/view-all.json')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            setMeals(data)})
        }, [])
    
    const allMeals = [];
    
    for (const currentMeal of meals) {
        allMeals.push(
            <div className="meal-card">
            <ShowMealComponent
                recipeId={currentMeal.recipe_id}
                title={currentMeal.title}   
                image={currentMeal.image}
                ingredients={currentMeal.ingredients}  
                instructions={currentMeal.instructions}
                tips={currentMeal.tips} 
            />
            <FavoriteButtonComponent
                recipeId={currentMeal.recipe_id}
            />
        
            <br/><br/>
            </div>
        
        );
    }

    return (
        <div id="all-container">
            <div id="top" className="row-md-12">LunchBoxy's Meals</div>
            <div className="grid">{allMeals}</div>
        </div>
    );

    }
    
    ReactDOM.render(<MealContainer />, document.getElementById('container')); 