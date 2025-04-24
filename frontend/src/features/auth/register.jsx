import React, {useState} from "react";
import axios from "axios";

const Register = () => {
    const [form, setForm] = useState({
        username: "",
        email: "",
        firstName: "",
        lastName: "",
        password: "",
    });
    
    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    }
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:5173/api/auth/users/register/", form);
            console.log(response.data);
        } catch (error) {
            console.error("Error registering user:", error);
        }
    }
    
    
    return (
        <div className="register-container">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" name="username" placeholder="Username" value={form.username} onChange={handleChange} required />
                <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
                <input type="text" name="firstName" placeholder="First Name" value={form.firstName} onChange={handleChange} required />
                <input type="text" name="lastName" placeholder="Last Name" value={form.lastName} onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} required />
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default Register;