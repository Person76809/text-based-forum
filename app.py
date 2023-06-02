import tkinter as tk

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content

class ForumApp:
    def __init__(self):
        self.posts = []
        
        self.root = tk.Tk()
        self.root.title("4chan-like Forum")
        
        self.post_frame = tk.Frame(self.root)
        self.post_frame.pack(padx=10, pady=10)
        
        self.create_label = tk.Label(self.post_frame, text="Create a new post")
        self.create_label.pack()
        
        self.author_entry = tk.Entry(self.post_frame)
        self.author_entry.pack(pady=5)
        
        self.content_entry = tk.Text(self.post_frame, height=5, width=30)
        self.content_entry.pack(pady=5)
        
        self.create_button = tk.Button(self.post_frame, text="Create", command=self.create_post)
        self.create_button.pack(pady=5)
        
        self.view_frame = tk.Frame(self.root)
        self.view_frame.pack(padx=10, pady=10)
        
        self.view_label = tk.Label(self.view_frame, text="All Posts")
        self.view_label.pack()
        
        self.posts_listbox = tk.Listbox(self.view_frame, height=10, width=40)
        self.posts_listbox.pack(pady=5)
        
        self.scrollbar = tk.Scrollbar(self.view_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.posts_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.posts_listbox.yview)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)
        
        self.root.mainloop()
        
    def create_post(self):
        author = self.author_entry.get()
        content = self.content_entry.get("1.0", tk.END).strip()
        if author and content:
            post = Post(author, content)
            self.posts.append(post)
            self.posts_listbox.insert(tk.END, f"Author: {post.author}\n{post.content}\n")
            self.author_entry.delete(0, tk.END)
            self.content_entry.delete("1.0", tk.END)
        else:
            tk.messagebox.showerror("Error", "Please enter both author and content.")
            
if __name__ == "__main__":
    app = ForumApp()
