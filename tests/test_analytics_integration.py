import pytest


def insert_trade(
    flask_connection,
    *,
    symbol,
    open_time,
    close_time,
    trade_type,
    status,
    direction,
    open_price,
    close_price=None,
    risk=1.0,
    sl=None,
    tp=None,
    rr=None,
):
    flask_connection.execute(
        """
        INSERT INTO trades (
            symbol,
            open_time,
            close_time,
            type,
            status,
            sort,
            open_price,
            close_price,
            risk,
            SL,
            TP,
            RR,
            initial_risk
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            symbol,
            open_time,
            close_time,
            trade_type,
            status,
            direction,
            open_price,
            close_price,
            risk,
            sl,
            tp,
            rr,
            risk,
        ),
    )


def create_golden_dataset(flask_connection):
    trades = [
        # +2R
        {
            "symbol": "BTCUSD",
            "open_time": "2026-08-01 09:00",
            "close_time": "2026-08-01 10:00",
            "trade_type": "HTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 110,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": 2.0,
        },

        # -1R
        {
            "symbol": "BTCUSD",
            "open_time": "2026-08-02 09:00",
            "close_time": "2026-08-02 10:00",
            "trade_type": "MTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 95,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": -1.0,
        },

        # +1.5R
        {
            "symbol": "ETHUSD",
            "open_time": "2026-08-03 09:00",
            "close_time": "2026-08-03 10:00",
            "trade_type": "LTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 92.5,
            "risk": 5,
            "sl": 105,
            "tp": 90,
            "rr": 1.5,
        },

        # -0.5R
        {
            "symbol": "ETHUSD",
            "open_time": "2026-08-04 09:00",
            "close_time": "2026-08-04 10:00",
            "trade_type": "HTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 102.5,
            "risk": 5,
            "sl": 105,
            "tp": 90,
            "rr": -0.5,
        },

        # 0R
        {
            "symbol": "EURUSD",
            "open_time": "2026-08-05 09:00",
            "close_time": "2026-08-05 10:00",
            "trade_type": "LTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 100,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": 0.0,
        },

        # +3R
        {
            "symbol": "EURUSD",
            "open_time": "2026-08-06 09:00",
            "close_time": "2026-08-06 10:00",
            "trade_type": "MTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 115,
            "risk": 5,
            "sl": 95,
            "tp": 115,
            "rr": 3.0,
        },

        # -2R
        {
            "symbol": "BTCUSD",
            "open_time": "2026-08-07 09:00",
            "close_time": "2026-08-07 10:00",
            "trade_type": "HTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 110,
            "risk": 5,
            "sl": 105,
            "tp": 90,
            "rr": -2.0,
        },

        # +0.5R
        {
            "symbol": "AAPL",
            "open_time": "2026-08-08 09:00",
            "close_time": "2026-08-08 10:00",
            "trade_type": "LTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 102.5,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": 0.5,
        },

        # -1R
        {
            "symbol": "AAPL",
            "open_time": "2026-08-09 09:00",
            "close_time": "2026-08-09 10:00",
            "trade_type": "MTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 105,
            "risk": 5,
            "sl": 105,
            "tp": 90,
            "rr": -1.0,
        },

        # +1R
        {
            "symbol": "BTCUSD",
            "open_time": "2026-08-10 09:00",
            "close_time": "2026-08-10 10:00",
            "trade_type": "HTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 105,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": 1.0,
        },

        # +2.5R
        {
            "symbol": "ETHUSD",
            "open_time": "2026-08-11 09:00",
            "close_time": "2026-08-11 10:00",
            "trade_type": "LTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 87.5,
            "risk": 5,
            "sl": 105,
            "tp": 85,
            "rr": 2.5,
        },

        # -0.75R
        {
            "symbol": "EURUSD",
            "open_time": "2026-08-12 09:00",
            "close_time": "2026-08-12 10:00",
            "trade_type": "MTF",
            "status": "CLOSED",
            "direction": "LONG",
            "open_price": 100,
            "close_price": 96.25,
            "risk": 5,
            "sl": 95,
            "tp": 110,
            "rr": -0.75,
        },

        # +1.25R
        {
            "symbol": "BTCUSD",
            "open_time": "2026-08-13 09:00",
            "close_time": "2026-08-13 10:00",
            "trade_type": "HTF",
            "status": "CLOSED",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": 93.75,
            "risk": 5,
            "sl": 105,
            "tp": 90,
            "rr": 1.25,
        },

        # OPEN — must not affect closed performance metrics.
        {
            "symbol": "ETHUSD",
            "open_time": "2026-08-14 09:00",
            "close_time": None,
            "trade_type": "LTF",
            "status": "OPEN",
            "direction": "LONG",
            "open_price": 100,
            "close_price": None,
            "risk": 1,
            "sl": 95,
            "tp": 110,
            "rr": None,
        },

        # OPEN — must not affect closed performance metrics.
        {
            "symbol": "AAPL",
            "open_time": "2026-08-15 09:00",
            "close_time": None,
            "trade_type": "MTF",
            "status": "OPEN",
            "direction": "SHORT",
            "open_price": 100,
            "close_price": None,
            "risk": 1,
            "sl": 105,
            "tp": 90,
            "rr": None,
        },
    ]

    for trade in trades:
        insert_trade(
            flask_connection,
            symbol=trade["symbol"],
            open_time=trade["open_time"],
            close_time=trade["close_time"],
            trade_type=trade["trade_type"],
            status=trade["status"],
            direction=trade["direction"],
            open_price=trade["open_price"],
            close_price=trade["close_price"],
            risk=trade["risk"],
            sl=trade["sl"],
            tp=trade["tp"],
            rr=trade["rr"],
        )

    flask_connection.commit()


def test_analytics_requires_login(client):
    response = client.get("/analytics")

    assert response.status_code == 302
    assert response.location.endswith("/setup")


def test_analytics_empty_database(authenticated_client):
    response = authenticated_client.get("/analytics")

    assert response.status_code == 200


def test_analytics_golden_dataset(
    authenticated_client,
    flask_connection,
):
    create_golden_dataset(flask_connection)

    response = authenticated_client.get("/analytics?period=all")

    assert response.status_code == 200
