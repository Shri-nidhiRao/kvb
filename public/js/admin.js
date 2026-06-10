document.addEventListener("DOMContentLoaded", () => {
    // Check Authentication
    const adminToken = localStorage.getItem('adminToken');
    if (!adminToken) {
        window.location.href = 'login.html';
        return;
    }

    // Determine the API base URL based on the current environment.
    // For localhost, we assume the server is running on port 5001.
    const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
        ? 'http://localhost:5001/api/blogs' 
        : '/api/blogs'; // Fallback

    const tableBody = document.getElementById("blogTableBody");
    const modal = document.getElementById("blogModal");
    const form = document.getElementById("blogForm");
    const modalTitle = document.getElementById("modalTitle");

    let blogs = [];

    // Fetch and render blogs
    const fetchBlogs = async () => {
        tableBody.innerHTML = `<tr><td colspan="4" class="loading-spinner"><i class="fas fa-spinner fa-spin fa-2x"></i><br>Loading blogs...</td></tr>`;
        try {
            const res = await fetch(API_BASE);
            if (!res.ok) throw new Error("Failed to fetch");
            blogs = await res.json();
            renderBlogs();
        } catch (error) {
            console.error("Error fetching blogs:", error);
            tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:red; padding: 2rem;">Error loading blogs. Make sure the Node server is running on localhost:5001.</td></tr>`;
        }
    };

    const renderBlogs = () => {
        if (blogs.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; padding: 2rem; color: #888;">No blogs found. Create your first blog!</td></tr>`;
            return;
        }

        tableBody.innerHTML = blogs.map(blog => `
            <tr>
                <td>
                    <div class="blog-title-cell">
                        <img src="${blog.imageUrl || 'https://via.placeholder.com/150'}" alt="Thumbnail">
                        <div>
                            <strong style="display:block; font-size:1.1rem; margin-bottom:4px;">${blog.title}</strong>
                            <span style="color:#888; font-size:0.85rem;">
                                ${blog.tags ? blog.tags.map(t => `<span style="background:#eee; padding:2px 6px; border-radius:4px; margin-right:4px;">${t}</span>`).join('') : ''}
                            </span>
                        </div>
                    </div>
                </td>
                <td>${blog.author || 'Admin'}</td>
                <td>${new Date(blog.date).toLocaleDateString()}</td>
                <td>
                    <div class="action-btns">
                        <button class="btn-icon btn-edit" onclick="editBlog('${blog.id}')" title="Edit"><i class="fas fa-edit"></i></button>
                        <button class="btn-icon btn-delete" onclick="deleteBlog('${blog.id}')" title="Delete"><i class="fas fa-trash-alt"></i></button>
                    </div>
                </td>
            </tr>
        `).join('');
    };

    // Open Modal
    const openModal = () => {
        modal.classList.add("active");
    };

    const closeModal = () => {
        modal.classList.remove("active");
        form.reset();
        document.getElementById("blogId").value = "";
        modalTitle.innerText = "Create New Blog";
    };

    document.getElementById("openModalBtn").addEventListener("click", () => {
        closeModal(); // Reset form
        openModal();
    });
    
    document.getElementById("closeModalBtn").addEventListener("click", closeModal);
    document.getElementById("cancelBtn").addEventListener("click", closeModal);

    // Form Submit (Create or Update)
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const id = document.getElementById("blogId").value;
        const tagsStr = document.getElementById("blogTags").value;
        
        const blogData = {
            title: document.getElementById("blogTitle").value,
            imageUrl: document.getElementById("blogImage").value,
            author: document.getElementById("blogAuthor").value,
            tags: tagsStr ? tagsStr.split(',').map(t => t.trim()) : [],
            content: document.getElementById("blogContent").value,
            date: new Date().toISOString().split('T')[0] // Always set current date on update
        };

        const method = id ? "PUT" : "POST";
        const url = id ? `${API_BASE}/${id}` : API_BASE;

        try {
            const res = await fetch(url, {
                method: method,
                headers: { 
                    "Content-Type": "application/json",
                    "Authorization": \`Bearer \${adminToken}\`
                },
                body: JSON.stringify(blogData)
            });

            if (res.ok) {
                closeModal();
                fetchBlogs();
            } else {
                alert("Failed to save blog.");
            }
        } catch (error) {
            console.error("Error saving blog:", error);
            alert("Error communicating with the server.");
        }
    });

    // Edit Blog (Exposed to window for inline onclick)
    window.editBlog = (id) => {
        const blog = blogs.find(b => b.id === id);
        if (!blog) return;

        document.getElementById("blogId").value = blog.id;
        document.getElementById("blogTitle").value = blog.title;
        document.getElementById("blogImage").value = blog.imageUrl || '';
        document.getElementById("blogAuthor").value = blog.author || '';
        document.getElementById("blogTags").value = blog.tags ? blog.tags.join(', ') : '';
        document.getElementById("blogContent").value = blog.content || '';

        modalTitle.innerText = "Edit Blog";
        openModal();
    };

    // Delete Blog
    window.deleteBlog = async (id) => {
        if (!confirm("Are you sure you want to delete this blog? This action cannot be undone.")) return;

        try {
            const res = await fetch(`${API_BASE}/${id}`, { 
                method: "DELETE",
                headers: { "Authorization": `Bearer ${adminToken}` }
            });
            if (res.ok) {
                fetchBlogs();
            } else {
                alert("Failed to delete blog.");
            }
        } catch (error) {
            console.error("Error deleting blog:", error);
            alert("Error communicating with the server.");
        }
    };

    // Logout
    window.logout = (e) => {
        if (e) e.preventDefault();
        localStorage.removeItem('adminToken');
        window.location.href = 'login.html';
    };

    // Initial fetch
    fetchBlogs();
});
