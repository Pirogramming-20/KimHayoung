//json file로부터 items를 동적으로 받아온다.
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

//update the list with the given items
function displayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}
//create html list item from the given data item 
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item_thumbnail" />
        <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function onButtonClick(event, items){
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key == null || value == null){
        return;
    }
    displayItems(items.filter(item => item[key] === value));

}

function setEventListener(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', event => onButtonClick(event, items));


}

// main
loadItems() 
.then(items => {
    displayItems(items);
    setEventListener(items)
})
.catch(console.log);
