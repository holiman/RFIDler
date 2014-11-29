/***************************************************************************
 * A copy of the GNU GPL is appended to this file.                         *
 *                                                                         *
 * This licence is based on the nmap licence, and we express our gratitude *
 * for the work that went into producing it. There is no other connection  *
 * between RFIDler and nmap either expressed or implied.                   *
 *                                                                         *
 ********************** IMPORTANT RFIDler LICENSE TERMS ********************
 *                                                                         *
 *                                                                         *
 * All references to RFIDler herein imply all it's derivatives, namely:    *
 *                                                                         *
 * o RFIDler-LF Standard                                                   *
 * o RFIDler-LF Lite                                                       *
 * o RFIDler-LF Nekkid                                                     *
 *                                                                         *
 *                                                                         *
 * RFIDler is (C) 2013-2014 Aperture Labs Ltd.                             *
 *                                                                         *
 * This program is free software; you may redistribute and/or modify it    *
 * under the terms of the GNU General Public License as published by the   *
 * Free Software Foundation; Version 2 ("GPL"), BUT ONLY WITH ALL OF THE   *
 * CLARIFICATIONS AND EXCEPTIONS DESCRIBED HEREIN.  This guarantees your   *
 * right to use, modify, and redistribute this software under certain      *
 * conditions.  If you wish to embed RFIDler technology into proprietary   *
 * software or hardware, we sell alternative licenses                      *
 * (contact sales@aperturelabs.com).                                       *
 *                                                                         *
 * Note that the GPL places important restrictions on "derivative works",  *
 * yet it does not provide a detailed definition of that term.  To avoid   *
 * misunderstandings, we interpret that term as broadly as copyright law   *
 * allows.  For example, we consider an application to constitute a        *
 * derivative work for the purpose of this license if it does any of the   *
 * following with any software or content covered by this license          *
 * ("Covered Software"):                                                   *
 *                                                                         *
 * o Integrates source code from Covered Software.                         *
 *                                                                         *
 * o Is designed specifically to execute Covered Software and parse the    *
 * results (as opposed to typical shell or execution-menu apps, which will *
 * execute anything you tell them to).                                     *
 *                                                                         *
 * o Includes Covered Software in a proprietary executable installer.  The *
 * installers produced by InstallShield are an example of this.  Including *
 * RFIDler with other software in compressed or archival form does not     *
 * trigger this provision, provided appropriate open source decompression  *
 * or de-archiving software is widely available for no charge.  For the    *
 * purposes of this license, an installer is considered to include Covered *
 * Software even if it actually retrieves a copy of Covered Software from  *
 * another source during runtime (such as by downloading it from the       *
 * Internet).                                                              *
 *                                                                         *
 * o Links (statically or dynamically) to a library which does any of the  *
 * above.                                                                  *
 *                                                                         *
 * o Executes a helper program, module, or script to do any of the above.  *
 *                                                                         *
 * This list is not exclusive, but is meant to clarify our interpretation  *
 * of derived works with some common examples.  Other people may interpret *
 * the plain GPL differently, so we consider this a special exception to   *
 * the GPL that we apply to Covered Software.  Works which meet any of     *
 * these conditions must conform to all of the terms of this license,      *
 * particularly including the GPL Section 3 requirements of providing      *
 * source code and allowing free redistribution of the work as a whole.    *
 *                                                                         *
 * As another special exception to the GPL terms, Aperture Labs Ltd. grants*
 * permission to link the code of this program with any version of the     *
 * OpenSSL library which is distributed under a license identical to that  *
 * listed in the included docs/licenses/OpenSSL.txt file, and distribute   *
 * linked combinations including the two.                                  *
 *                                                                         *
 * Any redistribution of Covered Software, including any derived works,    *
 * must obey and carry forward all of the terms of this license, including *
 * obeying all GPL rules and restrictions.  For example, source code of    *
 * the whole work must be provided and free redistribution must be         *
 * allowed.  All GPL references to "this License", are to be treated as    *
 * including the terms and conditions of this license text as well.        *
 *                                                                         *
 * Because this license imposes special exceptions to the GPL, Covered     *
 * Work may not be combined (even as part of a larger work) with plain GPL *
 * software.  The terms, conditions, and exceptions of this license must   *
 * be included as well.  This license is incompatible with some other open *
 * source licenses as well.  In some cases we can relicense portions of    *
 * RFIDler or grant special permissions to use it in other open source     *
 * software.  Please contact sales@aperturelabs.com with any such requests.*
 * Similarly, we don't incorporate incompatible open source software into  *
 * Covered Software without special permission from the copyright holders. *
 *                                                                         *
 * If you have any questions about the licensing restrictions on using     *
 * RFIDler in other works, are happy to help.  As mentioned above, we also *
 * offer alternative license to integrate RFIDler into proprietary         *
 * applications and appliances.  These contracts have been sold to dozens  *
 * of software vendors, and generally include a perpetual license as well  *
 * as providing for priority support and updates.  They also fund the      *
 * continued development of RFIDler.  Please email sales@aperturelabs.com  *
 * for further information.                                                *
 * If you have received a written license agreement or contract for        *
 * Covered Software stating terms other than these, you may choose to use  *
 * and redistribute Covered Software under those terms instead of these.   *
 *                                                                         *
 * Source is provided to this software because we believe users have a     *
 * right to know exactly what a program is going to do before they run it. *
 * This also allows you to audit the software for security holes (none     *
 * have been found so far).                                                *
 *                                                                         *
 * Source code also allows you to port RFIDler to new platforms, fix bugs, *
 * and add new features.  You are highly encouraged to send your changes   *
 * to the RFIDler mailing list for possible incorporation into the         *
 * main distribution.  By sending these changes to Aperture Labs Ltd. or   *
 * one of the Aperture Labs Ltd. development mailing lists, or checking    *
 * them into the RFIDler source code repository, it is understood (unless  *
 * you specify otherwise) that you are offering the RFIDler Project        *
 * (Aperture Labs Ltd.) the unlimited, non-exclusive right to reuse,       *
 * modify, and relicense the code.  RFIDler will always be available Open  *
 * Source, but this is important because the inability to relicense code   *
 * has caused devastating problems for other Free Software projects (such  *
 * as KDE and NASM).  We also occasionally relicense the code to third     *
 * parties as discussed above. If you wish to specify special license      *
 * conditions of your contributions, just say so when you send them.       *
 *                                                                         *
 * This program is distributed in the hope that it will be useful, but     *
 * WITHOUT ANY WARRANTY; without even the implied warranty of              *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the RFIDler   *
 * license file for more details (it's in a COPYING file included with     *
 * RFIDler, and also available from                                        *
 *   https://github.com/ApertureLabsLtd/RFIDler/COPYING                    *
 *                                                                         *
 ***************************************************************************/

// Author: Adam Laurie <adam@aperturelabs.com>

#include "HardwareProfile.h"
#include "rfidler.h"
#include "analogue.h"
#include "clock.h"


void init_adc(BOOL slow)
{
    CloseADC10();
    SetChanADC10( ADC_CH0_NEG_SAMPLEA_NVREF | ADC_CH0_POS_SAMPLEA_AN11);
    if(slow)
       OpenADC10( ADC_CONFIG1, ADC_CONFIG2_SLOW, ADC_CONFIG3, ADC_CONFIGPORT, ADC_CONFIGSCAN );
    else
        OpenADC10( ADC_CONFIG1, ADC_CONFIG2, ADC_CONFIG3, ADC_CONFIGPORT, ADC_CONFIGSCAN );
    EnableADC10();
    // wait for first read to complete
    while ( !mAD1GetIntFlag() )
        ;
}

/**
 * analogue_sample
 * @param length - number of (requested) samples
 * @param local_read - switch off local_read to sniff transaction with external clock
 * @return the number of BYTES written to the buffer.
 **/
unsigned int analogue_sample(unsigned int length, BOOL local_read)
{
    unsigned int i, scale;
    // we have a static buffer for samples, so if we want to see more, scale sample rate accordingly
    scale= (((length - 1) / sizeof(DataBuff))) +1 ;
    /**
     The way this is implemented,
     - If length less than 8096, scale will be == 1
     - If length more than 8096 (but less than 2*8096), scale == 2
     - So, if length = 9000, every other sample will be stored, to a total
     of 4500.
     */
    init_adc(FAST);
    FakeRead= TRUE;
    // start read
    if(!local_read)
        SnifferMode= TRUE;
    get_tag_uid(TmpBuff);
    // get one sample per byte - max value from ADC is 1024 so divide by 4 (>>2)
    // add in digital sample state (BIT_1) and reader bit period (BIT_0) for display purposes
    for(i= 0 ; i < length ; ++i)
    {
        DataBuff[i / scale]= (((read_adc() + DC_OFFSET) >> 2) & SAMPLEMASK) + (READER_DATA << 1) + ReaderPeriod;
    }

    FakeRead= FALSE;
    SnifferMode= FALSE;
    stop_HW_clock();
    return i;
}

/**
 * digital_sample
 * @param length - number of (requested) samples.
 * @param local_read - switch off local_read to sniff transaction with external clock
 * @return the number of BYTES written to the buffer.
 **/
unsigned int digital_sample(unsigned int n_samples, BOOL local_read)
{
    unsigned int i, scale;
    // we have a static buffer for samples, 8096 BYTE. 
    // we'll save each sample as 
    // - 1 bit digital sample sate
    // - 1 bit reader bit period
    //Thus, stuffing 4 samples in each byte, allowing 32k samples
    if((n_samples >> 2) > sizeof(DataBuff)){
        n_samples = sizeof(DataBuff) << 2;
    }
    init_adc(FAST);
    FakeRead= TRUE;
    // start read
    if(!local_read)
        SnifferMode= TRUE;
    get_tag_uid(TmpBuff);
    // get one sample per byte - max value from ADC is 1024 so divide by 4 (>>2)
    // add in digital sample state (BIT_1) and reader bit period (BIT_0) for display purposes
    BYTE read_value = 0;
    BYTE a0,a1,a2,a3;
    for(i= 0 ; i < (n_samples >> 2) ; i++)
    {
        //Always sample for whole bytes (4 values)
        // 748 + 60 : 1011101100  .. = 808 >> 2 : 202
        read_value = read_adc();
        a0 = (((read_value + DC_OFFSET) >> 2) & SAMPLEMASK) + (READER_DATA << 1) + ReaderPeriod;
        a1 = (((read_adc() + DC_OFFSET) >> 2) & SAMPLEMASK) + (READER_DATA << 1) + ReaderPeriod;
        a2 = (((read_adc() + DC_OFFSET) >> 2) & SAMPLEMASK) + (READER_DATA << 1) + ReaderPeriod;
        a3 = (((read_adc() + DC_OFFSET) >> 2) & SAMPLEMASK) + (READER_DATA << 1) + ReaderPeriod;
        DataBuff[i] =   ((a0 & 0x3) << 6) |
                        ((a1 & 0x3) << 4) |
                        ((a2 & 0x3) << 2) |
                        (a3 & 0x3);

    }
    FakeRead= FALSE;
    SnifferMode= FALSE;
    stop_HW_clock();

    return i;
}
/**
 @xml_indented_array_expand
 * @param item - tag name
 * @param data - data buffer
 * @param bitmask - the bitmask to use
 * @length the length in *bytes* of data buffer (not bits)
 * @indent - xml indentation
 * This is a utility function to send bits, which have been packed into a buffer,
 * as individual hex-encoded numbers. The function sends four numbers for each
 * byte, shifting the bitmask two steps right each time
 */
void xml_indented_array_expand(BYTE *item, BYTE *data, BYTE bitmask, unsigned int length, BYTE* indent)
{
    xml_header(item, indent);

    unsigned int i;
    unsigned int a0,a1,a2,a3;
    for(i= 0 ; i < length ; ++i)
    {
        if(!(i % 8))
        {
            UserMessage("%s", "\r\n");
            space_indent(*indent);
        }
        //Pick out the bit, convert to 1/0
        a0 = (data[i] & bitmask) >> 6;
        a1 = (data[i] & (bitmask >> 2)) >> 4;
        a2 = (data[i] & (bitmask >> 4)) >> 2;
        a3 = (data[i] & (bitmask >> 6));
        UserMessageNum("%02lx", a0);
        UserMessageNum("%02lx", a1);
        UserMessageNum("%02lx", a2);
        UserMessageNum("%02lx", a3);
    }
    xml_footer(item, indent, NEWLINE);

}
void digital_xml_out(unsigned int length)
{
    BYTE indent= 0, tmp;
    char data_rate[10] = {0};

    xml_version();
    xml_header("RFIDler_Samples", &indent);
    xml_item_text("Description", "RFIDler Digital Coil Samples", &indent);

    xml_header("Tag", &indent);
    xml_item_text("Description", "Tag Settings", &indent);
    xml_header("Tag_Type", &indent);
    xml_item_text("Description", "Tag Type", &indent);
    xml_item_text("Data", (BYTE *) TagTypes[RFIDlerConfig.TagType], &indent);
    xml_footer("Tag_Type", &indent);
    xml_header("Modulation", &indent);
    xml_item_text("Description", "Modulation Scheme", &indent);
    xml_item_text("Data", (BYTE *) ModulationSchemes[RFIDlerConfig.Modulation], &indent);
    xml_footer("Modulation", &indent);
    xml_header("Data_Rate", &indent);
    xml_item_text("Description", "Data Rate (Frame Clocks)", &indent);
    snprintf(data_rate, 10, "%d",RFIDlerConfig.DataRate);
    xml_item_text("Data", data_rate, &indent);
    xml_footer("Data_Rate", &indent);
    xml_footer("Tag", &indent);

    // pots
    xml_header("Pots", &indent);
    xml_item_text("Description", "Potentiometer Settings (Decimal)", &indent);
    xml_header("Pot_High", &indent);
    xml_item_text("Description", "Potentiometer High Setting", &indent);
    get_mcp414_wiper(0, FALSE, &tmp);
    xml_item_decimal("Data", tmp, &indent);
    xml_footer("Pot_High", &indent);
    xml_header("Pot_Low", &indent);
    xml_item_text("Description", "Potentiometer Low Setting", &indent);
    get_mcp414_wiper(1, FALSE, &tmp);
    xml_item_decimal("Data", tmp, &indent);
    xml_footer("Pot_Low", &indent);
    xml_footer("Pots", &indent);

    // samples
    xml_header("Samples", &indent);
    xml_item_text("Description", "Time Based Sample Arrays", &indent);

    // reader circuit
    xml_header("Reader_Output", &indent);
    xml_item_text("Description", "Analogue Circuit Digital Reader Output (HIGH/LOW)", &indent);
    xml_indented_array_expand("Data", DataBuff, 0x80 , length, &indent);
    xml_footer("Reader_Output", &indent);
    // bit period
    xml_header("Bit_Period", &indent);
    xml_item_text("Description", "Modulation Scheme Bit Period (TICKS)", &indent);
    xml_indented_array_expand("Data", DataBuff, 0x40 , length, &indent);
    xml_footer("Bit_Period", &indent);
    xml_footer("Samples", &indent);

    // end
    xml_footer("RFIDler_Samples", &indent);
    UserMessage("%s", "\r\n");

}
// output analogue buffer as XML
void analogue_xml_out(unsigned int length)
{
    BYTE indent= 0, tmp;
    char data_rate[10] = {0};
    if(length > sizeof(DataBuff))
        length= sizeof(DataBuff);

    // header
    xml_version();
    xml_header("RFIDler_Samples", &indent);
    xml_item_text("Description", "RFIDler Analogue Coil Samples", &indent);

    // tag
    xml_header("Tag", &indent);
    xml_item_text("Description", "Tag Settings", &indent);
    xml_header("Tag_Type", &indent);
    xml_item_text("Description", "Tag Type", &indent);
    xml_item_text("Data", (BYTE *) TagTypes[RFIDlerConfig.TagType], &indent);
    xml_footer("Tag_Type", &indent);
    xml_header("Modulation", &indent);
    xml_item_text("Description", "Modulation Scheme", &indent);
    xml_item_text("Data", (BYTE *) ModulationSchemes[RFIDlerConfig.Modulation], &indent);
    xml_footer("Modulation", &indent);
    xml_header("Data_Rate", &indent);
    xml_item_text("Description", "Data Rate (Frame Clocks)", &indent);
    snprintf(data_rate, 10, "%d",RFIDlerConfig.DataRate);
    xml_item_text("Data", data_rate, &indent);
    xml_footer("Data_Rate", &indent);
    xml_footer("Tag", &indent);

    // pots
    xml_header("Pots", &indent);
    xml_item_text("Description", "Potentiometer Settings (Decimal)", &indent);
    xml_header("Pot_High", &indent);
    xml_item_text("Description", "Potentiometer High Setting", &indent);
    get_mcp414_wiper(0, FALSE, &tmp);
    xml_item_decimal("Data", tmp, &indent);
    xml_footer("Pot_High", &indent);
    xml_header("Pot_Low", &indent);
    xml_item_text("Description", "Potentiometer Low Setting", &indent);
    get_mcp414_wiper(1, FALSE, &tmp);
    xml_item_decimal("Data", tmp, &indent);
    xml_footer("Pot_Low", &indent);
    xml_footer("Pots", &indent);


    // samples
    xml_header("Samples", &indent);
    xml_item_text("Description", "Time Based Sample Arrays", &indent);
    // raw coil
    xml_header("Coil_Data", &indent);
    xml_item_text("Description", "Analogue Circuit Raw Data (HEX)", &indent);
    xml_item_array("Data", DataBuff, SAMPLEMASK, length, &indent);
    xml_footer("Coil_Data", &indent);
    // reader circuit
    xml_header("Reader_Output", &indent);
    xml_item_text("Description", "Analogue Circuit Digital Reader Output (HIGH/LOW)", &indent);
    xml_item_array("Data", DataBuff, BIT_1, length, &indent);
    xml_footer("Reader_Output", &indent);
    // bit period
    xml_header("Bit_Period", &indent);
    xml_item_text("Description", "Modulation Scheme Bit Period (TICKS)", &indent);
    xml_item_array("Data", DataBuff, BIT_0, length, &indent);
    xml_footer("Bit_Period", &indent);
    xml_footer("Samples", &indent);
    
    // end
    xml_footer("RFIDler_Samples", &indent);
    UserMessage("%s", "\r\n");
}

// determine resonant frequency of coil
unsigned long analogue_frequency(void)
{
    unsigned int i, high, tmp, highest= 0;
    float freq;
    unsigned long tmpfreq, best= 0;

    stop_HW_clock();

    // sample coil voltage at a reange of frequencies
    for(freq= (float) 100000 ; freq < (float) 151000 ; freq += (float) 1000)
    {
        tmpfreq= (unsigned long) ((1L/freq) * 100000000L);
        InitHWReaderClock(OC_TOGGLE_PULSE, tmpfreq / 2L, tmpfreq, RWD_STATE_ACTIVE);
        init_adc(FAST);
        Delay_us(100000);
        for(i= 0, high= 0 ; i < 10000 ; ++i)
        {
            tmp= read_adc();
            if(i > 2000 && tmp > high)
                high= tmp;
        }
        UserMessageNum("%d: ", (unsigned long) freq);
        UserMessageNum("%d\r\n", high);
        if(high > highest)
        {
            highest= high;
            best= (unsigned long) freq;
        }
        stop_HW_clock();
        CloseADC10();
    }
    return best;
}
