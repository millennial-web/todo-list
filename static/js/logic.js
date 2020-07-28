function goGetResults(){

    let buscar_tipo = d3.select("#buscarTipo").property("value")

    d3.json(`/api/consultar/${buscar_tipo}`).then(json=>{

        let selection = d3
        .select("#rcontainer")
        .selectAll("li")
        .data(json)

        selection
        .enter()
        .append("li")
        .merge(selection)
        .text(d=>d.desc)

        selection.exit().remove()

    })
}

function insertTodo(){
    let texto = d3.select("#todo").property("value")
    let tipo = d3.select("#tipoTodo").property("value")

    nuevo_dato = {
        "texto": texto,
        "tipo": tipo
    }

    let configOption = {
        method: "POST",
        body : JSON.stringify(nuevo_dato),
        headers:{
            "Content-type": "application/json"
        }
    }

    d3.json("/api/insert",configOption).then(json=>{
        console.log(json)
        goGetResults()
    })

}

goGetResults();
d3.select("#buscarTipo").on("change", goGetResults);
d3.select("#addTodo").on("click", insertTodo);


