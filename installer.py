 
 ​import​ ​os​, ​sys​, ​time​, ​socket​, ​json 
 ​from​ ​os​ ​import​ ​popen​, ​system 
 ​from​ ​time​ ​import​ ​sleep 
  
 ​# Normal 
 ​black​=​"​\033​[0;30m" 
 ​red​=​"​\033​[0;31m" 
 ​green​=​"​\033​[0;32m" 
 ​bgreen​=​"​\033​[1;32m" 
 ​yellow​=​"​\033​[0;33m" 
 ​blue​=​"​\033​[0;34m" 
 ​purple​=​"​\033​[0;35m" 
 ​cyan​=​"​\033​[0;36m" 
 ​bcyan​=​"​\033​[1;36m" 
 ​white​=​"​\033​[0;37m" 
 ​nc​=​"​\033​[00m" 
  
 ​version​=​"1.6" 
  
 ​ask​ ​=​ ​green​ ​+​ ​'['​ ​+​ ​white​ ​+​ ​'?'​ ​+​ ​green​ ​+​ ​'] '​+​ ​yellow 
 ​success​ ​=​ ​yellow​ ​+​ ​'['​ ​+​ ​white​ ​+​ ​'√'​ ​+​ ​yellow​ ​+​ ​'] '​+​green 
 ​error​ ​=​ ​blue​ ​+​ ​'['​ ​+​ ​white​ ​+​ ​'!'​ ​+​ ​blue​ ​+​ ​'] '​+​red 
 ​info​=​ ​yellow​ ​+​ ​'['​ ​+​ ​white​ ​+​ ​'+'​ ​+​ ​yellow​ ​+​ ​'] '​+​ ​cyan 
 ​info2​=​ ​green​ ​+​ ​'['​ ​+​ ​white​ ​+​ ​'•'​ ​+​ ​green​ ​+​ ​'] '​+​ ​purple 
  
 ​# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator 
  
 ​logo​=​f''' 
 ​{​red​}​  _____       _____  _     _     _                
 ​{​cyan​}​ |  __ \     |  __ \| |   (_)   | |               
 ​{​yellow​}​ | |__) |   _| |__) | |__  _ ___| |__   ___ _ __  
 ​{​blue​}​ |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__| 
 ​{​red​}​ | |   | |_| | |    | | | | \__ \ | | |  __/ |    
 ​{​yellow​}​ |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|    
 ​{​green​}​         __/ |                          ​{​cyan​}​[v1.6] 
 ​{​cyan​}​        |___/                   ​{​red​}​[By KasRoudra] 
 ​'''
