const showLogin = document.getElementById('login-toggle');
    
    showLogin.addEventListener('click', () => {
        const loginForm = document.getElementById('login-form');
        
        if (loginForm.style.display === 'none') {
            loginForm.style.display = 'block';
        } else {
            loginForm.style.display = 'none';
        }
        });

        
const showCreate = document.getElementById('create-toggle');
    
showCreate.addEventListener('click', () => {
    const createForm = document.getElementById('create-acct-form');
    
    if (createForm.style.display === 'none') {
        createForm.style.display = 'block';
    } else {
        createForm.style.display = 'none';
    }
    });



    