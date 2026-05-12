const BLOCKS = {

hero: `
<style>
.hero{
    min-height:100vh;
    background:black;
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    font-family:Arial;
}

.hero h1{
    font-size:70px;
    margin:0;
}

.hero p{
    font-size:24px;
    color:#999;
}

.hero button{
    padding:15px 30px;
    background:#00ffcc;
    border:none;
    margin-top:20px;
    font-size:18px;
    cursor:pointer;
}
</style>

<section class="hero">
    <div>
        <h1>{{title}}</h1>
        <p>{{subtitle}}</p>
        <button>{{button}}</button>
    </div>
</section>
`,

navbar: `
<style>
.navbar{
    background:#111;
    color:white;
    padding:20px;
    font-family:Arial;
}

.logo{
    font-size:24px;
    font-weight:bold;
}
</style>

<nav class="navbar">
    <div class="logo">
        {{logo}}
    </div>
</nav>
`,

cards: `
<style>
.cards{
    display:flex;
    gap:20px;
    padding:50px;
    background:#f5f5f5;
    font-family:Arial;
}

.card{
    background:white;
    padding:30px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,0.1);
}
</style>

<section class="cards">

    <div class="card">
        <h2>{{title}}</h2>
        <p>
            Servicio profesional premium
        </p>
    </div>

</section>
`,

footer: `
<style>
.footer{
    background:#111;
    color:white;
    padding:30px;
    text-align:center;
    font-family:Arial;
}
</style>

<footer class="footer">
    <p>{{copyright}}</p>
</footer>
`

};
