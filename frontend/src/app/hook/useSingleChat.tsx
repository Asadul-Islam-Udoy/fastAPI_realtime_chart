"use client";
import { useEffect, useRef } from "react";

export default function useSingleChat(
  senderId: number | undefined,
  receiverId: number,
  onMessage: (msg: any) => void
) {
  const socket = useRef<WebSocket | null>(null);

  useEffect(() => {
    if (!senderId) return;
    const ws = new WebSocket(
      `ws://localhost:8000/api/v1/messages/ws/chat/${senderId}/${receiverId}`
    );
    socket.current = ws;

    ws.onopen = () => {
      console.log("WebSocket connected");
    };

    ws.onmessage = (event) => {
      console.log("Raw WS message data:", event.data);
      try {
        const data = JSON.parse(event.data);
        console.log("Received WS message:", data);
        onMessage(data);
      } catch (err) {
        console.error("Failed to parse WS message", err);
      }
    };

    ws.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    return () => {
      ws.close();
    };
  }, [senderId, receiverId, onMessage]);

  const sendMessage = (content: string) => {
    if (socket.current?.readyState === WebSocket.OPEN) {
      console.log("Sending WS message:", content);
      socket.current.send(JSON.stringify({ content }));
    } else {
      console.warn(
        "WebSocket not open. Current state:",
        socket.current?.readyState
      );
    }
  };

  return { sendMessage };
}
