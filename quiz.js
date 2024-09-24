let currentQuestion = 0;
let score = 10;
let category = '';
let questions = [];
let options = [];
let answers = [];

const pythonQuestions = ["01. What is dictionary in Python?", "02. Which keyword is used to handle exceptions?", /* Add more questions */];
const pythonOptions = [
    ["A. Ordered collection", "B. Unordered key-value pairs", "C. Unique items", "D. Characters"],
    ["A. Catch", "B. Handle", "C. Try", "D. Except"],
    // Add more options
];
const pythonAnswers = ["B", "C"]; // Add answers

const mathsQuestions = ["What is the next number in the sequence: 2,6,12,20,30?", /* Add more */];
const mathsOptions = [
    ["A. 40", "B. 42", "C. 36", "D. 46"],
    // Add more options
];
const mathsAnswers = ["B"]; // Add answers

const dsaQuestions = ["Which data structure follows LIFO?", /* Add more */];
const dsaOptions = [
    ["A. Queue", "B. Stack", "C. Array", "D. Linked list"],
    // Add more options
];
const dsaAnswers = ["B"]; // Add answers

function startQuiz(selectedCategory) {
    category = selectedCategory;
    if (category === 'python') {
        questions = pythonQuestions;
        options = pythonOptions;
        answers = pythonAnswers;
    } else if (category === 'maths') {
        questions = mathsQuestions;
        options = mathsOptions;
        answers = mathsAnswers;
    } else if (category === 'dsa') {
        questions = dsaQuestions;
        options = dsaOptions;
        answers = dsaAnswers;
    }

    document.querySelector('.two').style.display = 'none';
    document.getElementById('quiz-container').style.display = 'block';
    showQuestion();
}

function showQuestion() {
    document.getElementById('question').textContent = questions[currentQuestion];
    let optionsHTML = '';
    options[currentQuestion].forEach((option, index) => {
        optionsHTML += `<button onclick="checkAnswer('${String.fromCharCode(65 + index)}')">${option}</button><br>`;
    });
    document.getElementById('options').innerHTML = optionsHTML;
}

function checkAnswer(selectedOption) {
    if (selectedOption === answers[currentQuestion]) {
        document.getElementById('result').textContent = 'Correct!';
    } else {
        document.getElementById('result').textContent = `Wrong! Correct answer: ${answers[currentQuestion]}`;
        score -= 2;
    }

    document.getElementById('next-question').style.display = 'block';
}

function nextQuestion() {
    currentQuestion++;
    if (currentQuestion < questions.length) {
        showQuestion();
        document.getElementById('result').textContent = '';
        document.getElementById('next-question').style.display = 'none';
    } else {
        document.getElementById('result').textContent = `Quiz completed! Your score: ${score}`;
        document.getElementById('options').style.display = 'none';
        document.getElementById('next-question').style.display = 'none';
    }
}
