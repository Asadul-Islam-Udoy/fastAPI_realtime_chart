import Image from "next/image";
import MessageBox from "./components/MessageBox";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex  flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="sdf.js logo"
          width={180}
          height={38}
          priority
        />

        <div className="w-full max-w-sm min-w-[200px]">
          <div className="md:w-[500px] w-full">
            <input
              type="text"
              className="md:w-[500px] w-full pl-3 pr-10 py-4 bg-transparent placeholder:text-slate-400 text-slate-600 text-sm border border-slate-200 rounded-md transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
              placeholder="Type here..."
            />

            <div className="w-full mt-2 cursor-pointer bg-blue-400 flex justify-content-center align-items-center">
              <button className="p-2 cursor-pointer text-[red] w-full">
                 Send
              </button>
            </div>
          </div>
        </div>
              <MessageBox/>
      </main>

    </div>
  );
}
