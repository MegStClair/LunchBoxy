// props = title, image, ingredients, instructions, tips
function FillingComponent(props) {
    return (
        <div id="filling">
        <h1>{ props.title }</h1>
        <img src={ props.image } width={500}/>
        <p> <b>Ingredients: </b> { props.ingredients }</p>
        <p> <b>Directions: </b>{ props.instructions }</p>
    
        <p><b>Tip!</b> { props.tips }</p>
        
        </div>
    );
    }

function SidesComponent(props) {
        return (
            <div id="sides">
            <h2>{ props.title }</h2>
            <img src={ props.image } width={200}/>
            </div>
        );
        }


function RecipeContainer(props) {
    return (
        <div id="lunch">
        <FillingComponent {...props.filling}/>
            
            <div id="crunchy">
            <SidesComponent {...props.crunchy}/>
            </div>
    
            <div id="fresh">
            <SidesComponent {...props.fresh}/>
            </div>

            <div id="fresh2">
            <SidesComponent {...props.fresh2}/>
            </div>

        </div>
    
    )
}



fetch('/lunch-idea.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<RecipeContainer {...recipes}/>, document.getElementById('container'));

});

// to be able to "change" item- use class on divs and grab elements by class, render stuff in a for loop (avoid rep)
