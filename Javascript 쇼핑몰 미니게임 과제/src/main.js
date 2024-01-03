//json file로부터 items를 동적으로 받아온다.
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

functiondisplayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}
function createHTMLString(item) {
    return `

    `;
}
// main
loadItems() 
.then(items => {
    displayItems(items);
    setEventListener(items)
})
.catch(console.log);
