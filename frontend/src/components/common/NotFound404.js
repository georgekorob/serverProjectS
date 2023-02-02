import React from 'react';

export default function NotFound404({location}) {
    return (
        <div>
            <h2>Страница по адресу '{location.pathname}' не найдена.</h2>
        </div>
    )
}
