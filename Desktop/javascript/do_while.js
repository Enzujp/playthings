const cats = ['leopard', 'jaguar', 'lion', 'hyena']

let myFavoriteCats = "my favourite cats are: ";

let i = 0;

do {
    if (i === cats.length -1){
        myFavoriteCats += `and ${cats[i]}.`;
    } else{
        myFavoriteCats += `${cats[i]}, `;
    }


i++;

} while (i < cats.length);

console.log(myFavoriteCats);