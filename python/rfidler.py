#!/usr/bin/env python

"""
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
 ***************************************************************************

*/

// Author: Adam Laurie <adam@aperturelabs.com>

"""

import sys
import select
import os
import time
import xml.etree.ElementTree as ET
import collections
from matplotlib import pyplot
import numpy
import RFIDler


# global flags
Quiet = False

# global constants
ADC_To_Volts = 0.012890625  # 3.3 / 256
POT_To_Volts = 0.019607843  # 5 / 255


def output(message):
    if not Quiet:
        print message

def count_changes(data):
    periods =  []
    count =0
    prev = data[0]
    for v in data:
        if prev == v:
            count += 1
        else:
            periods.append(count)
            prev = v
            count = 1
    return periods

def store_data(data,  filename_prefix = "dump"):
    root = ET.fromstring(''.join(data))
    # wrap it in an ElementTree instance, and save as XML
    tree = ET.ElementTree(root)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "%s_%s.xml" % (filename_prefix, timestr)
    tree.write(filename)
    output("Wrote dump to %s" % filename)

def load_data(fname):
    try:
        with open(fname, "r") as f:
            lines = f.readlines()
    except Exception, e:
        return [False, str(e)]

    return [True, lines]



def plot_autocorr(axis, data, length  = 400, color = 'g'):
    """
    See 
    http://stackoverflow.com/questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation
    """
    
    result = numpy.correlate( data,data[:length], mode='full')
    autoc = result[length-1:]

    axis.plot(range(len(autoc)) , autoc , range(len(autoc)) , "-", color=color,label = "Autocorrelation (size %d)" % length)

def show_bitstream(bit_periods,  reader_out):
    x = 0
    binary_out = ""
    for i in bit_periods:
        bit = reader_out[x]
        binary_out += str(bit)
        x += bit_periods[i]

    print("Bitstream: %s" % binary_out)
    # Hex stream
    # Show as a sliding window.
    for offset in range (0,8):
        # Split in chunks of eight
        hexbinary = [binary_out[i:i+8] for i in range(offset, len(binary_out), 8)]
        _hex = ["%02x" % int(bin, 2) for bin in hexbinary]
        print("Hexstream (offset %d): %s" % (offset," ".join(_hex)))



def plot_data(data, digital=False):
    
    # create graphic objects
#    fig, ax1 = pyplot.subplots()
    ax_corr = None

    fig, (ax1, ax_corr) = pyplot.subplots(2)

    # label 
    ax1.set_xlabel('Sample Number')
    ax1.legend(loc=2)

    # get xml sections
    xml = ET.fromstring(''.join(data))
    samples = xml.find('Samples')
    tag = xml.find('Tag')
    pots = xml.find('Pots')

    # Set title
    title = tag.find('Tag_Type')
    pyplot.title('RFIDler - ' + title.find('Data').text)


    def readxml_data(x):
        if samples.find(x) is None:
            return None
        data = samples.find(x).find('Data')
        out = data.text.replace(' ', '')
        out = map(ord, out.decode("hex"))
        return out

    # raw coil data
    coil_out = readxml_data('Coil_Data')
    # reader HIGH/LOW
    reader_out = readxml_data('Reader_Output')
    # bit period
    bitperiod_out = readxml_data('Bit_Period')
    
    pyplot.xlim(0, len(reader_out))

    if coil_out:
        #Raw coil readings
        coil_out = [x * ADC_To_Volts for x in coil_out]
        x = range(len(coil_out))

        # ADC scale needs to match volts (5v / 3.3v)
        ax1.set_ylim(-5, 256 * 1.515151515)
        
        ax1.set_ylabel('Signal Strength (ADC)')

        # we need second subplot for voltage scale
        ax2 = ax1.twinx()
        ax2.plot(x, coil_out, color='b', label="Raw Data")

        # pot settings
        color = 'r'
        for element in 'Pot_High', 'Pot_Low':
            pot_data = pots.find(element).find('Data').text
            p_volts = float(pot_data) * POT_To_Volts
            ax2.axhline(y=p_volts,color=color,label= ' %0.2fv (Pot: %s)' % (p_volts,pot_data))
            color = 'm'


        # volts scale up to 5.0v as that is max pot setting
        # note that the ADC will clip at 3.3v, so although we can use a higher pot setting,
        # we can't see token samples above 3.3v
        ax2.set_ylim(0, 5.0)
        ax2.set_ylabel('Signal Strength (Volts)', rotation=270)
        ax2.legend(loc=1)
    
    x = range(len(reader_out))
    #Use a counter to help calc bit period
    count = 0
    prev = reader_out[0]
    bitcounts = []

    # convert to value that will show on scale
    def rescale(upperval,lowerval, selectval):
        def fun(x):
            if x > selectval:
                return upperval
            return lowerval
        return fun

    reader_out = map(rescale(258,4,0), reader_out)

    
    ax_corr2 = ax_corr.twinx()

    plot_autocorr(ax_corr, reader_out, 400, color='b')
    plot_autocorr(ax_corr2, reader_out, 2000, color='g')

    ax_corr.legend(loc=1)
    ax_corr2.legend(loc=2)

    # Show reader logic
    ax1.plot(x, reader_out, '-', color='g', label='Reader Logic')
    # show compressed version
    reader_out = map(rescale(320,300, 257), reader_out)

    ax1.plot(x, reader_out, '-', color='g')

    bit_periods =  count_changes(bitperiod_out)


    # show bit period as single vertical stripe
    z = 0
    i = 0
    while i < len(bit_periods): 
        if i % 2 == 0:
            ax1.axvspan(z, z+ bit_periods[i], facecolor = 'r', alpha = 0.1)
        z += bit_periods[i]
        i += 1

    # find first stripe and add legend
    for i in range(len(bitperiod_out)):
        if (bitperiod_out[i]):
            break
    legend = tag.find('Data_Rate')
    data = legend.find('Data').text
    ax1.text(i + (bit_periods[0] / 2), -10, 'Bit Period\n%s FCs' % data, color='r', alpha=0.5, rotation=270,
             ha='center', va='top')

    # Show the most common bit-toggling periods observed 
    reader_bit_periods =  count_changes(reader_out)
    print("Most common bit periods:")
    print("\n".join(["%d : %d" % kv for kv in collections.Counter(reader_bit_periods).most_common(10)]))

    #Display the bitstream and hexstream
    show_bitstream(bit_periods,  map(rescale(1,0,301), reader_out))


    fig.canvas.set_window_title('RFIDler plot')
    pyplot.show()

if len(sys.argv) < 3:
    print """
 usage: {0} <PORT> <COMMAND> [ARGS] [COMMAND [ARGS] ...]

   Commands:

     DEBUG <OFF|ON>                           Show serial comms
     FLASH[P] <IMAGE.HEX>                     Set bootloader mode and flash IMAGE.HEX [in Production mode]
     PLOT [-n] [-d] <SAMPLES>                 Plot raw coil samples 
                                                 <SAMPLES>      The number of samples to request
                                                 -n             No local clock (sniffmode)
                                                 -d             digital mode, enables up to 32k samples
     STORE [-n] [-d] <SAMPLES> <file_prefix>  Save raw coil samples to file
                                                 <SAMPLES>      The number of samples to request
                                                 -n             No local clock (sniffmode)
                                                 -d             digital mode, enables up to 32k samples
                                                 <file_prefix>  The prefix for the file to save into
     LOAD <file>                              Load and plot saved sample-file        
     PROMPT <MESSAGE>                         Print MESSAGE and wait for <ENTER>
     QUIET                                    Supress confirmation of sent command (show results only)
     SLEEP <SECONDS>                          Pause for SECONDS
     TEST                                     Run hardware manufacting test suite
    
   Commands will be executed sequentially.
   Unrecognised commands will be passed directly to RFIDler.
   Commands with arguments to be passed directly should be quoted. e.g. "SET TAG FDXB"
""".format(*sys.argv)
    exit(True)

port = sys.argv[1]
rfidler = RFIDler.RFIDler()
result, reason = rfidler.connect(port)
if not result:
    print 'Warning - could not open serial port:', reason

current = 2
# process each command
while current < len(sys.argv):
    command = sys.argv[current].upper()
    current += 1
    if command == 'DEBUG':
        if sys.argv[current].upper() == 'ON':
            rfidler.Debug = True
        else:
            if sys.argv[current].upper() == 'OFF':
                rfidler.Debug = False
            else:
                print 'Unknown option:', sys.argv[current]
                exit(True)
        current += 1
        continue

    if command == 'FLASH' or command == 'FLASHP':
        if not os.path.exists('/dev/hidraw1'):
            result, reason = rfidler.command('BL')
            if not result:
                print 'could not set bootloader mode!'
                exit(True)
        rfidler.disconnect()
        time.sleep(1)
        if os.path.exists('/dev/hidraw1'):
            print 'bootloader mode - flashing...'
            os.system('mphidflash -r -w %s' % sys.argv[current])
        else:
            print 'bootloader not detected!'
            exit(True)
        print 'Waiting for reboot...'
        while 42:
            result, reason = rfidler.connect(port)
            if result:
                result, data = rfidler.command('PING')
                if result:
                    break
        if command == 'FLASHP':
            time.sleep(1)
            print 'Load next board'
            # wait for disconnect
            while 42:
                try:
                    time.sleep(.5)
                    result, data = rfidler.command('PING')
                    if not result:
                        break
                except:
                    break
            print 'Waiting for board...'
            # wait for new board in normal or bootloader mode
            while 42:
                result, reason = rfidler.connect(port)
                if result:
                    result, data = rfidler.command('PING')
                    if result:
                        break
                rfidler.disconnect()
                if os.path.exists('/dev/hidraw1'):
                    break
            current -= 1
            continue
        current += 1
        continue

    if command == 'XKCD':
        pyplot.xkcd()
        continue
    if command in ['PLOT', 'STORE']:
        #Check switches, starts with -
        digital = False
        no_local_clock = False
        print("Next two arguments:", sys.argv[current:current+2])
        if "-d" in sys.argv[current:current+2]:
            digital = True
        if "-n" in sys.argv[current:current+2]:
            no_local_clock = True

        _cmd = "ANALOGUE"
        if digital:
            _cmd = "DIGITAL"
            current += 1
        if no_local_clock:
            _cmd += "N"
            current += 1
        
        num_samples = int(sys.argv[current])
        current += 1
        result, data = rfidler.command('%s %d' % (_cmd, num_samples))
        if result:
            if command == "PLOT":
                plot_data(data)
            else:# 'STORE'
                filename_prefix = sys.argv[current]
                store_data(data, filename_prefix)
                current += 1
        else:
            output('Failed: ' + data)
        continue
    if command == 'LOAD':
        result, data = load_data(sys.argv[current])
        current += 1
        if result:
            plot_data(data)
        else:
            output('Failed: ' + data)
        continue

    if command == 'PROMPT':
        raw_input(sys.argv[current])
        current += 1
        continue

    # perform hardware tests for manufacturing assurance
    # requires hardware to be placed on test jig
    if command == 'TEST':
        test = 1
        print 'Testing H/W. Hit <ESC> to end.'
        while 42:
            print 'waiting for board...'
            while 42:
                rfidler.disconnect()
                result, reason = rfidler.connect(port)
                if result:
                    break
                if os.path.exists('/dev/hidraw1'):
                    print 'bootloader mode - flashing...'
                    os.system(
                        'mphidflash -r -w /home/software/unpacked/RFIDler/firmware/Pic32/RFIDler.X/dist/debug/production/RFIDler.X.production.hex')

            os.system('clear')
            test_result = 'Pass'
            print 'Starting test', test
            for x in 'PING', \
                     'DEBUGOFF 0', \
                     'DEBUGON 4', \
                     'DEBUGON 2', 'SET TAG HITAG2', 'UID', 'DEBUGOFF 2', \
                     'DEBUGON 3', 'SET TAG INDALA64', 'UID', 'DEBUGOFF 3', \
                     'TEST-WIEGAND', 'TEST-SC', 'TEST-SD', \
                     'SET TAG HID26', 'ENCODE 12345678 HID26', 'EMULATOR BG', 'WIEGAND-OUT OFF', 'TEST-WIEGAND-READ 1':
                print '  Test %s - ' % x,
                sys.stdout.flush()
                for z in range(10):
                    result, data = rfidler.command(x)
                    if result:
                        break
                print result, data
                if not result:
                    test_result = 'Fail!'
            # now wait for board to change
            os.system('figlet ' + test_result)
            test += 1
            print 'load next board'
            while 42:
                try:
                    result, data = rfidler.command('PING')
                    if not result:
                        break
                except:
                    break
        continue

    if command == 'SLEEP':
        output('Sleeping for %s seconds' % sys.argv[current])
        time.sleep(float(sys.argv[current]))
        current += 1
        continue

    if command == 'TERMINAL':
        while 42:
            while rfidler.Connection.inWaiting():
                sys.stdout.write(rfidler.Connection.readline(1))
                sys.stdout.flush()
            # send typed characters
            while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                x = sys.stdin.read(1)
                rfidler.Connection.write(x)
                # read back echo
                x = rfidler.Connection.read(1)
                sys.stdout.write(x)
                sys.stdout.flush()

    # set quiet flag so we only see responses, not sent commands
    if command == 'QUIET':
        Quiet = True
        continue

    # catchall - pass command directly
    output("sending '%s'" % command)
    sys.stdout.flush()
    result, data = rfidler.command(command)
    if result:
        for line in data:
            print line
    else:
        output('Failed: ' + data)
    continue
