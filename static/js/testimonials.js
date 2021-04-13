const testimonialsContainer = document.querySelector('.testimonials-container');
const testimonial = testimonialsContainer.querySelector('.testimonial');
const username = testimonialsContainer.querySelector('.username');
const role = testimonialsContainer.querySelector('.role');

const testimonials = [{
        "name": "Stephen",
        "position": "Web developer",
        "text": "Braams creation  made it easy and fun to choose a corporate logo for my business"
    },
    {
        "name": "Murichu",
        "position": "Entrepreneurs",
        "text": "This guys are amazing designers that delivered the task exactly how we needed it, do yourselves a favor and use their services, you will not be disappointed by the work delivered. They will go the extra mile to make sure that you are happy. We will surely work again with them!"
    },
    {
        "name": "Mary",
        "position": "Freelancer",
        "text": "Braams Creation is always my number one choice when i need work done perfectly according to my specification"
    },
    {
        "name": "Agnes",
        "position": "Store Owner",
        "text": "I am amazed by the quality of products made at Braams Creations"
    },
];
let idx = 1;


function updateTestimonial() {
    let { name, position, photo, text } = testimonials[idx];

    testimonial.innerHTML = text;
    logo.src = photo;
    username.innerHTML = name;
    role.innerHTML = position;

    idx++;
    if (idx > testimonials.length - 1) {
        idx = 0;
    }
}

setInterval(updateTestimonial, 10000);