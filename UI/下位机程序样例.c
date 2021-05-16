//========================================================包函文件
#include "c8051F020.h"     //包含C8051F020系列单片机硬件信息的头文件
#include "absacc.h"     //绝对地址访问相关的头文件
#include "intrins.h"     //nop等函数要求的头文件
#include "math.h"     //算数函数头文件
#include "data_define.c"
#include "Init_Device.c"
//========================================================常量定义
#define    	LED1  XBYTE[0x2000]  //第1位数码管端口地址
#define     LED2  XBYTE[0x2001]  //第2位数码管端口地址
#define     LED3  XBYTE[0x2002]  //第3位数码管端口地址
#define     LED4  XBYTE[0x2003]  //第4位数码管端口地址
#define     ADC0804_port XBYTE[0x0000]  //模数转换电路端口地址
#define		DAC0832_port XBYTE[0x6000]  //数模转换电路端口地址
#define		TIME_L	0xfd	//T/C1计数值,比特率为9600
#define		TIME_H	0xfd

//=====================================================全局变量定义
float y1; //温度换算后值
uchar num_arry[]={0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90,0x7f}; //数值显示段码数据
uchar idata set_high,set_low;    //控制温度设置高、低位数据暂存器
float temperature_val_H;   //控制温度设定值整数位
float temperature_val_L; 	 //控制温度设定值小数位
float temperature_val; //控制温度设定值
uchar read[8];//读指令暂存数组
uchar send[8];//发指令暂存数组
uchar idata temperature_read;   //读取温度值
uchar idata temperature_read_H;   //温度读数整数位
uchar idata temperature_read_L;   //温度读数小数位
uchar idata delaytime;//延时时间
uchar rcv_state;
uchar rcv_count;
uchar workflag;
uchar DAout;
bit DAoutflag;
bit read_flag;

bit ischeck;
bit temp_ctrlflag ;//温度控制标志位
bit isdelaystart  ;//延时启动标志位
bit isdelaystop   ;//延时停止标志位

//=========================================================函数定义
void    delay1(uint cont);
void    delay2(uint cont);
void    delay_m(void);
//void    display(uchar loc,uchar num);
//void    Timer_Init(void);
void    tem_ctrl(void);//温度控制任务
//void    tem_set(void);//启动设置温度
//void    tem_measure(void);//温度数据采集
//void    tem_display(uchar fun); //温度显示
void	ADCprg(void);//温度数据采集
void 	UART_init(void);//串口通信初始化
void 	Temperature(void);	//温度数值计算
void 	display3(void);//温度数值显示	
void	cmd(void);//上位机命令
void 	cmdsend(void);//发送指令至上位机



void	set_temp();//温度设置
void	set_addtemp1();//温度加1
void	set_subtemp1();//温度减一
void	set_delaystart();//延时启动设置
void	set_delaystop();//延时停止设置
void	DA_ctrl();//DA输出控制信号函数
void	temp_ask();//温度查询
void	delaystart_ask();//延时启动查询
void	delaystop_ask();//延时停止查询
void	workstate_ask();//工作状态查询
//====================================================主循环
void main(void)
{

	delay2(1);
	Init_Device(); //初始化串口，单片机，定时器
	UART_init();
	LED1=LED2=LED3=LED4=0xff; 	
    DAC0832_port=0x80;
	temp_ctrlflag = 0;
	rcv_state=0;
	DAoutflag=0;
	while(1)
	{
		ADCprg();			//温度数据采集
		Temperature();		//温度数值计算
		display3();			//温度数值显示	
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		tem_ctrl();
		else
			{if(DAoutflag == 1)
		    	DAC0832_port = DAout;
			else 
				DAC0832_port = 0x80;}
		delay1(5000);

	}
}
//=============================================命令接受函数
void cmd() interrupt 4
{	
	uchar temp;
	read_flag=0;
	ES0=0;	
	read_flag=0;
	while(read_flag==0)
	{
	 if(RI0)
		{	
			RI0=0;
			temp = SBUF0;
			switch(rcv_state)
			{
				case 0:
				if(temp == 67)
				rcv_state = 1;
				break;
				case 1:
				if(temp==79)
				rcv_state = 2;
				else 
				rcv_state = 0;
				break;
				case 2:
				if(temp==77)
				{
					rcv_state = 3;
					rcv_count = 3;
					read[7] = 22;
				}
				else rcv_state =0;
				break;
				case 3:
				read[3-rcv_count] =temp;
				rcv_count--;
				if(rcv_count == 0)
					{rcv_state =0;
					read_flag=1;}
				break;
			 }
		}
    }
 
	if(read_flag == 1)
	{
		switch(read[0])
		{
		case 0xa0:
			set_temp();
			break;
		case 0xa1:
			set_addtemp1();
			break;
		case 0xa2:
			set_subtemp1();
			break;
		case 0xa3:
			temp_ctrlflag=~temp_ctrlflag;
			workstate_ask();
			if(temp_ctrlflag==0)
 		    DAC0832_port=0x80;
			break;
		case 0xa4:
		    DAC0832_port=0x80;
			temp_ctrlflag = 0;
			set_delaystart();
			workstate_ask();
			break;
		case 0xa5:
			temp_ctrlflag = 1;
			set_delaystop();
			 DAC0832_port=0x80;
			 workstate_ask();
			break;
		case 0xa6:
			DA_ctrl();
			break;
		case 0xa8:
			ischeck=1;
			temp_ask();
			break;
		case 0xaa:
			delaystart_ask();
			break;
		case 0xab:
			delaystop_ask();
			break;
		case 0xae:
			workstate_ask();
			break;
		}
	}

  ES0=1;
}
//=============================================发送指令
void cmdsend()
{	
	uchar i;
	EA = 0;
	 	for(i = 0;i < 6;i++)
		{
	 		SBUF0 = send[i];
	 		while(TI0==0);
			TI0 = 0;
		}
	EA = 1;	
}
//=============================================温度控制任务
void tem_ctrl(void)
{
if(y1>temperature_val)//读出的值大于设定值时 
	{	DAC0832_port=0x00; 	} //降温
else if(y1<temperature_val)
	{DAC0832_port=0xff;	}//升温
else
	 DAC0832_port=0x80;
	 
	 delay2(100);
}

//===============================================串口通信初始化
void UART_init()
{
    SCON0 = 0x50;        //串口方式1
    TMOD = 0x20;        // 定时器使用方式2自动重载
    TH1 = 0xfd;    //9600波特率对应的预设数，定时器方式2下，TH1=TL1
    TL1 = 0xfd;

    EA=1;//开总中断
    ES0=1;//开串口中断
    REN0=1;
    SM10=1;
    SM00=0;
    TR1 = 1;//开启定时器，开始产生波特率
}
//===============================================温度数据采集、计算、显示
void ADCprg(void)
{
	ADC0804_port=0x00;		//启动A/D转换
	delay1(3000);		//调用延时函数等待转换结束
	temperature_read=ADC0804_port;		//读取A/D转换结果	
	delay1(3000);
}
void Temperature(void)
{	
	y1=temperature_read*100;
	y1=y1/255;
}
void display3(void)		
{
	uchar  i;		//定义变量存放计算结果
	uchar  j;	
	uchar  a;
	uchar  b;	
	i=y1/10;        //分离十位
    j=y1-(i*10);        //分离个位
	a=(y1*10)-i*100-j*10;
	b=(y1-i*10-j)*100-a*10;
	temperature_read_H=i*10+j;
	temperature_read_L=a*10+b;
	LED3=num_arry[j];
	LED4=num_arry[i];
	LED2=num_arry[a];
	LED1=num_arry[b];

}
//===========================================DA输出控制信号函数
//void	DA_ctrl(uchar DActrl)
//{	
//	DAC0832_port = DActrl;
//}
//====================软件短延时的函数，参数（cont无符号字符型）为循环次数
void delay1(uint cont)
{
 	uint i;   
 	for(i=0;i<cont;i++); 
}
//===============================软件长延时的函数，参数（cont无符号字符型）乘以1000为循环次数
void delay2(uint cont)
{
 	long i;  
 	for(i=0;i<cont*10;i++);
}
//====================软件延时n秒
void delay_m()
{	
	unsigned int i ;
		ES0=1;
		workstate_ask();
	for(i = 0;i < delaytime; )
	{
		ADCprg();			//温度数据采集
		Temperature();		//温度数值计算
		display3();			//温度数值显示	
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		{tem_ctrl();}
		if(isdelaystop==1){
		delaystop_ask();}
		if(isdelaystart==1){
		delaystart_ask();}
		delay1(5000);
		delay2(1800);
		ADCprg();			
		Temperature();	
		display3();			
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		{tem_ctrl();}
		delay2(2000);
		ADCprg();			
		Temperature();	
		display3();			
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		{tem_ctrl();}
		delay2(2000);
		ADCprg();			
		Temperature();	
		display3();			
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		{tem_ctrl();}
		delay2(1800);	
		ADCprg();			
		Temperature();	
		display3();			
		if(ischeck == 1)
		{temp_ask();}
		if(temp_ctrlflag == 1)
		{tem_ctrl();}	
		delay2(1225);
	    delaytime -=1;

	}
	temp_ctrlflag =~ temp_ctrlflag;
}
//===========================================温度设定
void set_temp()
{
   temperature_val_L = read[2];
   temperature_val_H = read[1];
   temperature_val = temperature_val_H+temperature_val_L/100 ;
}
//===========================================温度设定加1
void	set_addtemp1()
{
	temperature_val += 1;
}
//===========================================温度设定减1
void	set_subtemp1()
{
	temperature_val -= 1;
}
//===========================================延时启动控制
void	set_delaystart()
{	
	isdelaystart= 1;
	isdelaystop = 0;
	temp_ctrlflag = 0;
	delaytime = read[1]*60+read[2];
	delay_m();
	isdelaystart= 0;
}
//===========================================延时停止控制
void	set_delaystop()
{	
	isdelaystart=0;
	isdelaystop= 1;
	temp_ctrlflag = 1;
	delaytime = read[1]*60+read[2];
	delay_m();
	isdelaystop= 0;

}
//===========================================温度查询
void	temp_ask()
{
	ADCprg();
	send[0] = 'C';
	send[1] = 'O';
	send[2] = 'M';
	send[3] = 0xa8; 
	send[4] = temperature_read_H;
	send[5] = temperature_read_L;
	cmdsend();

}
//===========================================延时启动时间查询
void	delaystart_ask()
{
	int delaytimes,delaytimem,delaytime1,delaytime2;
	delaytime1=delaytime;
    delaytime2=delaytime1/60;
	delaytimem=delaytime2;
	delaytimes=delaytime1-60*delaytime2;
	send[0] = 'C';
	send[1] = 'O';
	send[2] = 'M';
	send[3] = 0xaa; 
	send[4] = delaytimem;
	send[5] = delaytimes-1;
	cmdsend();
}
//===========================================延时停止时间查询
void	delaystop_ask()
{
	int delaytimes,delaytimem,delaytime1,delaytime2;
	delaytime1=delaytime;
    delaytime2=delaytime1/60;
	delaytimem=delaytime2;
	delaytimes=delaytime1-60*delaytime2;
	send[0] = 'C';
	send[1] = 'O';
	send[2] = 'M';
	send[3] = 0xab; 
	send[4] = delaytimem;
	send[5] = delaytimes-1;
	cmdsend();
}
//===========================================数模转换数据设置
void	DA_ctrl()
{	
	temp_ctrlflag=0;
	DAout = read[1];
	DAoutflag = ~DAoutflag;
}
//===========================================工作状态查询
void	workstate_ask()
{	
	workflag=128;
	if(temp_ctrlflag) {workflag = 1+workflag;}
	if(isdelaystop)  {workflag = 2+workflag;}
	if(isdelaystart)  {workflag=4+workflag;}
	send[0] = 'C';
	send[1] = 'O';
	send[2] = 'M';
	send[3] = 0xae; 
	send[4] = workflag;
	send[5] = 0xff;
	cmdsend();
}
