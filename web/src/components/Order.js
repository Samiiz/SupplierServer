import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Order() {
  const [orders, setOrders] = useState([]);
  const [newOrder, setNewOrder] = useState('');

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await axios.get('http://3.25.100.75:8000/api/v1/orders/', {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        });
        setOrders(response.data);
      } catch (error) {
        alert('주문 목록을 가져오는 데 실패했습니다.');
      }
    };

    fetchOrders();
  }, []);

  const handleAddOrder = async () => {
    try {
      await axios.post('http://3.25.100.75:8000/api/v1/orders/', { name: newOrder }, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      });
      alert('주문이 추가되었습니다.');
    } catch (error) {
      alert('주문 추가에 실패했습니다.');
    }
  };

  return (
    <div>
      <h2>주문 목록</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>{order.name}</li>
        ))}
      </ul>
      <input
        type="text"
        placeholder="새 주문"
        value={newOrder}
        onChange={(e) => setNewOrder(e.target.value)}
      />
      <button onClick={handleAddOrder}>주문 추가</button>
    </div>
  );
}

export default Order;
