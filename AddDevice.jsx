import React, { useState } from 'react';

function AddDevice() {
    const [deviceName, setDeviceName] = useState('');
    const [deviceType, setDeviceType] = useState('');
    const [location, setLocation] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/devices', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ device_name: deviceName, device_type: deviceType, location: location })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Device Name:
                <input type="text" value={deviceName} onChange={e => setDeviceName(e.target.value)} />
            </label>
            <label>
                Device Type:
                <input type="text" value={deviceType} onChange={e => setDeviceType(e.target.value)} />
            </label>
            <label>
                Location:
                <input type="text" value={location} onChange={e => setLocation(e.target.value)} />
            </label>
            <button type="submit">Add Device</button>
        </form>
    );
}

export default AddDevice;
