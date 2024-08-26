// app.js
document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');
    app.innerHTML = '<h1>Welcome to New Mina Indian Restaurant</h1>';
});


// index.html (React)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> New Mina Indian Restaurant</title>
</head>
<body>
    <div id="root"></div>
    <script src="bundle.js"></script>
</body>
</html>


    // app.js (React)
    import React from 'react';
    import ReactDOM from 'react-dom';

    const App = () => {
        return (
            <div>
                <header>
                    <h1>Welcome to New Mina Indian Restaurant</h1>
                    <nav>
                        <ul>
                            <li><a href="#home">Home</a></li>
                            <li><a href="#menu">Menu</a></li>
                            <li><a href="#contact">Contact</a></li>
                        </ul>
                    </nav>
                </header>
                <section id="home">
                    <h2>About Us</h2>
                    <p>Experience the authentic flavors of India at our restaurant. We offer a wide variety of traditional dishes made with fresh ingredients and aromatic spices.</p>
                </section>
                <section id="menu">
                    <h2>Our Menu</h2>
                    <ul>
                        <li>Butter Chicken</li>
                        <li>Paneer Tikka</li>
                        <li>Biryani</li>
                        <li>Gulab Jamun</li>
                    </ul>
                </section>
                <section id="contact">
                    <h2>Contact Us</h2>
                    <p>Email: info@myindianrestaurant.com</p>
                    <p>Phone: +123-456-7890</p>
                </section>
                <footer>
                    <p>© 2024 New Mina Indian Restaurant. All rights reserved.</p>
                </footer>
            </div>
        );
    };

    ReactDOM.render(<App />, document.getElementById('root'));
