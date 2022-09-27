function FillingComponent(props) {
    return (
        <div id="filling">
        <h1>{ props.title }</h1>
        <img src={ props.image } width={300}/>
        </div>
    );
    }


    function RecipeContainer(props) {
        return (
            <div id="lunch">
            <FillingComponent {...props.filling}/>
            </div>
        
        )
    }




    fetch('/lunch-idea.json')
.then((response) => response.json())
.then((recipes) => {
    ReactDOM.render(<RecipeContainer {...recipes}/>, document.getElementById('container'));

});
