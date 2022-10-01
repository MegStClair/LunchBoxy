//////////////////////// DISPLAY ALL MEALS ///////////////////////////////////////


function ShowMealComponent(props) {

    const [showDetails, setShowDetails] = React.useState(false)

    function handleShowDetails() {
        console.log('image clicked')

        setShowDetails (!showDetails) 
        
    }
    let details = null 
    if (showDetails===true) {
        details = (
        <div className="detais">
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


function MealContainer() {

    const [meals, setMeals] = React.useState([]);

    React.useEffect(() => {
        fetch('/view-all.json')
        .then((response) => response.json())
        .then((data) => {setMeals(data) 
            console.log("Data.meals =", data)})
        }, [])
    
    const fillingMeals = [];
    
    for (const currentMeal of meals) {
        fillingMeals.push(

            <ShowMealComponent
                title={currentMeal.title}   
                image={currentMeal.image}
                ingredients={currentMeal.ingredients}  
                instructions={currentMeal.instructions}
                tips={currentMeal.tips} 
            />
        );
    }

    return (
        <div className="grid">{fillingMeals}</div>
    );

    }
    
    ReactDOM.render(<MealContainer />, document.getElementById('container')); 