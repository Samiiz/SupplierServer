import React, { useState } from 'react';
import axios from 'axios';

function SignUp() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignUp = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://3.25.100.75:8000/api/v1/signup/', {
        email,
        password,
      });
      alert('회원가입 성공!');
    } catch (error) {
      alert('회원가입 실패');
    }
  };

  return (
    <div>
      <h2>회원가입</h2>
      <form onSubmit={handleSignUp}>
        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">회원가입</button>
      </form>
    </div>
  );
}

export default SignUp;
