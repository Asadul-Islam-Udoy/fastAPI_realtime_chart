import type { FC } from "react";

interface MessageBoxProps {}

const MessageBox: FC<MessageBoxProps> = ({}) => {
  return (
    <>
      <div className="border pl-4 shadow h-[400px] md:w-[500px] w-full overflow-x-hidden">
          <div className=" md:p-4 w-full">
            <div className="flex m-2 gap-2">
              <img className="w-[30px] h-[30px] rounded-full" src="" />
              1
            </div>
            <p className="md:w-[200px]  w-[200px] break-all">
              hi, Asadul islam, how are you?
            </p>
          </div>
          <div className="w-full break-all md:ml-[53%] ml-[30%] ">
            <div className=" w-full md:ml-[35%] ml-[48%] flex m-2 gap-2">
              <img className="w-[30px] h-[30px] rounded-full" src="" />
              2
            </div>
            <p className="md:w-[200px] w-[150px] break-all">
              hello, Emon, I am Fine, about you? 
            </p>
          </div>
          
      </div>
    </>
  );
};
export default MessageBox;
