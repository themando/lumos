#!/usr/bin/env bash


# Converting Binary IQ samples to a Hex dump
for folder in ../data/backup/LTE_congestion/SanDiego/data/*

do 
    
    mkdir ../data/backup/LTE_congestion/SanDiego/hex
    mkdir ../data/backup/LTE_congestion/SanDiego/traces

    echo $(basename $folder)

    COUNTER=1
    for file in ../data/backup/LTE_congestion/SanDiego/data/"$(basename $folder)"/*
    do
        echo "$file"
        hexdump -e '"%07.7_Ax\n"' -e '"%07.7_ax " 16/1 "%02x " "\n"' $file > ../data/backup/LTE_congestion/SanDiego/hex/"$(basename "${file%.*}")".txt
        echo " $COUNTER "
        COUNTER=$[$COUNTER +1]

    done
    echo $(date)
    echo $(basename $folder)
    echo " *** First batch of Hexdump is done! *** "
    sleep 10

    COUNTER=1

    for file in ../data/backup/LTE_congestion/SanDiego/hex/*

    do
            text2pcap -D -l 147 $file ../data/backup/LTE_congestion/SanDiego/traces/"$(basename "${file%.*}")".pcap
            echo " $COUNTER "
        COUNTER=$[$COUNTER +1]

    done
    echo $(date)
    echo $(basename $folder)
    echo " *** First batch of PCAP is done! *** "
    sleep 10

    COUNTER=1

    for file in ../data/backup/LTE_congestion/SanDiego/traces/*

    do
            tshark -V -o "uat:user_dlts:\"User 0 (DLT=147)\",\"lte-rrc.bcch.dl.sch\",\"0\",\"\",\"0\",\"\"" -r $file -T json > ../data/backup/LTE_congestion/SanDiego/dl_bcch/"$(basename $folder)"/"$(basename "${file%.*}")".json
            echo " $COUNTER "
        COUNTER=$[$COUNTER +1]

    done
    echo $(date)
    echo $(basename $folder)
    echo " *** First batch of BCCH is done! *** "
    sleep 10

    COUNTER=1

    for file in ../data/backup/LTE_congestion/SanDiego/traces/*

    do
            tshark -V -o "uat:user_dlts:\"User 0 (DLT=147)\",\"lte-rrc.dl.ccch\",\"0\",\"\",\"0\",\"\"" -r $file -T json > ../data/backup/LTE_congestion/SanDiego/dl_ccch/"$(basename $folder)"/"$(basename "${file%.*}")".json
            echo " $COUNTER "
        COUNTER=$[$COUNTER +1]

    done
    echo $(date)
    echo $(basename $folder)
    echo " *** First batch of DL-CCCH is done! *** "
    sleep 10

    COUNTER=1

    for file in ../data/backup/LTE_congestion/SanDiego/traces/*

    do
            tshark -V -o "uat:user_dlts:\"User 0 (DLT=147)\",\"lte-rrc.ul.ccch\",\"0\",\"\",\"0\",\"\"" -r $file -T json > ../data/backup/LTE_congestion/SanDiego/ul_ccch/"$(basename $folder)"/"$(basename "${file%.*}")".json
            echo " $COUNTER "
        COUNTER=$[$COUNTER +1]

    done
    echo $(date)
    echo $(basename $folder)
    echo " *** First batch of UL-CCCH is done! *** "
    sleep 10

    rm -Rf ../data/backup/LTE_congestion/SanDiego/hex
    rm -Rf ../data/backup/LTE_congestion/SanDiego/traces


    sleep 5

done