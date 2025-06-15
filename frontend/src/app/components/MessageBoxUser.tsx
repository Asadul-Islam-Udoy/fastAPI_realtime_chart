import type { FC } from "react";
interface Message {
  sender_id: number;
  reviver_id: number;
  content: string;
  timestamp: string;
}
interface MessageBoxProps {
  messages: Message[];
  currentUserId?: number;
}

const MessageBox: FC<MessageBoxProps> = ({ messages, currentUserId }) => {
 return (
    <div className="border shadow h-[400px] md:w-[500px] w-full overflow-y-auto p-4 space-y-4">
      {messages?.map((msg, index) => {
        const isSender = msg.sender_id === currentUserId;
        return (
          <div
            key={index}
            className={`flex flex-col ${
              isSender ? "items-end" : "items-start"
            }`}
          >
            <div className="flex items-center gap-2">
              <img
                className="w-[30px] h-[30px] rounded-full"
                src="/avatar.png"
                alt="user"
              />
              <span className="text-sm font-semibold">
                {isSender ? "You" : `User ${msg.sender_id}`}
              </span>
            </div>
            <p className="bg-blue-100 text-black rounded px-3 py-2 max-w-[80%] break-words">
              {msg.content}
            </p>
            <span className="text-xs text-gray-500">
              {new Date(msg.timestamp).toLocaleTimeString()}
            </span>
          </div>
        );
      })}
    </div>
  );
};
export default MessageBox;
