const container = document.querySelector('#container');

const content = document.createElement('p');

const buttons = document.querySelectorAll('button');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        alert("I'm a pilot!!!");
    });
});

function alertFunction() {
    alert("Yes, boothang! It worked!");
}

// btn.addEventListener('click', alertFunction);


const newContent = document.createElement('h3');

const newDiv = document.createElement('div');

const newH1 = document.createElement('h1');

const newP = document.createElement('p');

newDiv.classList.add('newDiv');

newContent.classList.add('new');

newContent.style.color = 'blue';

newContent.textContent = "I'm a blue h3!";

newH1.textContent = "Me too!";

newP.textContent = "I'm in a div";

content.classList.add('content');

content.textContent = "Hey, I'm red!";

content.style.color = 'red';

newDiv.style.cssText = 'color: white; background: pink; border: 2px solid black;';

container.appendChild(content);
container.appendChild(newContent);

newDiv.appendChild(newH1);
newDiv.appendChild(newP);

container.appendChild(newDiv);