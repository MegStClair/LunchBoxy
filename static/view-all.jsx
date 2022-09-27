function ShowMealComponent(props) {
    return (
        <div className="meal">
        <h2>{ props.title }</h2>
        <img src={ props.image } width={300}/>
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
    console.log("meals state=", meals)
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