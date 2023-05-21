#include <OneWire.h>  //importando a biblioteca OneWire que faz comunicação com o sensor de temperatura
#include <DallasTemperature.h> //importando a biblioteca do sensor de temperatura da Dallas
#include "TimerOne.h" //importando a biblioteca do Timer1
#include <TimerThree.h> //importando a biblioteca do Timer3

#define dados 2 //definindo pino de dados como o 2
#define rele 11 //definindo pino do relé como o 11
 
OneWire oneWire(dados); //criando o objeto oneWire com atributo o pino dados
DallasTemperature sensors(&oneWire); //criando objeto sensors com atributo a referência do objeto oneWire
/********************************************************************/ 
float input; //criando variavel input 
float referencia = input; //criando variavel de referencia do degrau que inicialmente será igual a temperatura inicial da água

//criação da função que irá ser chamada na interrupção do timer de 2segundos que fará leitura e envio do sensor e outros dados
void atualizaSensor(){  
sensors.requestTemperatures(); //faz requisição da temperatura via objeto sensors
input = sensors.getTempCByIndex(0); //armazena temperatura em graus celsius na variavel input
Serial.print(input); //envia via serial a temperatura 
Serial.print(","); // separa por virgula
Serial.print(millis()); //envia tempo que o arduino está ativo desde que ligado pela função millis() (envia em milisegundos)
Serial.print(",");
Serial.println(referencia); //envia a referencia do degrau
}

void setup(void) 
{ 
 Timer1.initialize(1000000); //inicializa o timer1 com período de 1 segundo
 Timer3.initialize(2000000); //inicializa o timer3 com período de 2 segundos
 Serial.begin(9600);         //inicializa comunicação serial com baud rate 9600
 sensors.begin();            //inicializa o objeto sensors pelo método begin()
 Timer3.attachInterrupt(atualizaSensor); //cria uma interrupção com base no período do timer3 e passa a função a ser executada na interrupção
 delay(7000);                //da um delay de 7 segundos (obtermos dados da temperatura inicial, etc...)
 
 //degrau é dado no sistema
 Timer1.pwm(rele,1024);       //aciona o PWM do Timer1 na porta do relé, com duty cicle 100% (deixando passar toda a rede para a chaleira)
 referencia = 100.0;         //muda a temperatura de referencia como sendo 100°C (degrau foi dado no sistema)
} 
void loop(void) 
{
//não executa nada no loop, uma vez que a interrupção já será executada em loop a cada 2segundos 
}
