// API URLs
const API_URL = '/books';

// DOM elements
const sectionBooks = document.getElementById('section-books');
const sectionBookForm = document.getElementById('section-book-form');
const sectionReviewForm = document.getElementById('section-review-form');
const booksList = document.getElementById('books-list');
const bookForm = document.getElementById('book-form');
const reviewForm = document.getElementById('review-form');
const formTitle = document.getElementById('form-title');
const sortButton = document.getElementById('sort-button');
const addButton = document.getElementById('add-button');
const cancelFormButton = document.getElementById('cancel-form');
const cancelReviewButton = document.getElementById('cancel-review');
const alertsContainer = document.getElementById('alerts-container');

// Application state
let isEditing = false;
let currentSort = false;
let selectedRating = 0;

// Load books at startup
document.addEventListener('DOMContentLoaded', () => {
    loadBooks();
    setupEventHandlers();
});

// Setup event listeners
function setupEventHandlers() {
    // Sort Button
    sortButton.addEventListener('click', () => {
        currentSort = !currentSort;
        loadBooks();
    });

    // Add Book Button
    addButton.addEventListener('click', () => {
        showBookForm();
    });

    // Cancel Buttons
    cancelFormButton.addEventListener('click', hideBookForm);
    cancelReviewButton.addEventListener('click', hideReviewForm);

    // Book Form
    bookForm.addEventListener('submit', handleBookSubmit);
    
    // Review Form
    reviewForm.addEventListener('submit', handleReviewSubmit);

    // Stars for rating
    document.getElementById('rating-stars').addEventListener('click', (e) => {
        if (e.target.classList.contains('star')) {
            selectedRating = parseInt(e.target.dataset.value);
            updateStarsDisplay();
        }
    });
}

// Functions for book management
async function loadBooks() {
    try {
        const response = await fetch(`${API_URL}?sort=${currentSort}`);
        if (!response.ok) {
            throw new Error('Error loading books');
        }
        const books = await response.json();
        renderBooks(books);
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

function renderBooks(books) {
    booksList.innerHTML = '';
    
    if (books.length === 0) {
        booksList.innerHTML = '<tr><td colspan="5">No books found</td></tr>';
        return;
    }

    books.forEach(book => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${book.id}</td>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${renderRating(book.review)}</td>
            <td class="book-actions">
                <button class="edit-button" data-id="${book.id}">Edit</button>
                <button class="review-button" data-id="${book.id}">Review</button>
                <button class="delete-button delete" data-id="${book.id}">Delete</button>
            </td>
        `;
        booksList.appendChild(row);
    });

    // Add event listeners for buttons in rows
    document.querySelectorAll('.edit-button').forEach(btn => {
        btn.addEventListener('click', () => editBook(parseInt(btn.dataset.id)));
    });

    document.querySelectorAll('.review-button').forEach(btn => {
        btn.addEventListener('click', () => showReviewForm(parseInt(btn.dataset.id)));
    });

    document.querySelectorAll('.delete-button').forEach(btn => {
        btn.addEventListener('click', () => deleteBook(parseInt(btn.dataset.id)));
    });
}

function renderRating(rating) {
    if (!rating) {
        return '<span class="no-review">No review</span>';
    }
    
    let stars = '';
    for (let i = 0; i < rating; i++) {
        stars += '★';
    }
    return `<span class="stars">${stars}</span> (${rating}/5)`;
}

async function handleBookSubmit(e) {
    e.preventDefault();

    const bookData = {
        id: parseInt(document.getElementById('book-id').value),
        title: document.getElementById('book-title').value,
        author: document.getElementById('book-author').value,
        review: null
    };

    try {
        let response;
        if (isEditing) {
            response = await fetch(`${API_URL}/${bookData.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(bookData)
            });
        } else {
            response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(bookData)
            });
        }

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'An error occurred');
        }

        showAlert(
            isEditing ? 'Book updated successfully' : 'Book added successfully', 
            'success'
        );
        hideBookForm();
        loadBooks();
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

async function editBook(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        if (!response.ok) {
            throw new Error('Book not found');
        }
        const book = await response.json();
        
        document.getElementById('book-id').value = book.id;
        document.getElementById('book-title').value = book.title;
        document.getElementById('book-author').value = book.author;
        
        document.getElementById('book-id').disabled = true;
        formTitle.textContent = 'Edit Book';
        isEditing = true;
        showBookForm();
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

async function deleteBook(id) {
    if (!confirm('Are you sure you want to delete this book?')) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error('Error deleting the book');
        }
        
        showAlert('Book deleted successfully', 'success');
        loadBooks();
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

function showReviewForm(bookId) {
    document.getElementById('review-book-id').value = bookId;
    selectedRating = 0;
    updateStarsDisplay();
    
    sectionBooks.style.display = 'none';
    sectionReviewForm.style.display = 'block';
}

function updateStarsDisplay() {
    const stars = document.querySelectorAll('#rating-stars .star');
    stars.forEach((star, index) => {
        star.classList.toggle('selected', index < selectedRating);
    });
}

async function handleReviewSubmit(e) {
    e.preventDefault();
    
    const bookId = document.getElementById('review-book-id').value;
    
    if (selectedRating === 0) {
        showAlert('Please select a rating', 'error');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/${bookId}/review`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ review: selectedRating })
        });
        
        if (!response.ok) {
            throw new Error('Error adding the review');
        }
        
        showAlert('Review added successfully', 'success');
        hideReviewForm();
        loadBooks();
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

function showBookForm() {
    if (!isEditing) {
        bookForm.reset();
        document.getElementById('book-id').disabled = false;
        formTitle.textContent = 'Add Book';
    }
    
    sectionBooks.style.display = 'none';
    sectionBookForm.style.display = 'block';
}

function hideBookForm() {
    sectionBookForm.style.display = 'none';
    sectionBooks.style.display = 'block';
    isEditing = false;
}

function hideReviewForm() {
    sectionReviewForm.style.display = 'none';
    sectionBooks.style.display = 'block';
}

function showAlert(message, type) {
    const alert = document.createElement('div');
    alert.className = `alert ${type}`;
    alert.textContent = message;
    
    alertsContainer.appendChild(alert);
    
    // Remove alert after 3 seconds
    setTimeout(() => {
        alert.remove();
    }, 3000);
} 