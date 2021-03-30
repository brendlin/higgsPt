
def AddParameterScan(command,dimension,operator,scan_list) :

    def scanPointName(_op,i_scan) :
        return '{}_{}'.format(operator,i_scan).replace('-','m').replace('.','p')

    # If this is the first one, then make the first scan points
    if not command :
        for i_scan in scan_list :
            rwgt_name = scanPointName(operator,i_scan)
            command += 'launch --rwgt_name={}\n'.format(rwgt_name)
            command += '    set {} {} {}\n'.format(dimension,operator,i_scan)
        return command

    # otherwise, duplicate and modify existing launch commands
    launch_commands = []
    for launch in command.split('launch') :
        if not launch :
            continue
        for i_scan in scan_list :
            lines = launch.split('\n')

            # First line: Add to scan point name
            lines[0] = lines[0] + '_' + scanPointName(operator,i_scan)

            # Append the new set line
            lines.append('    set {} {} {}'.format(dimension,operator,i_scan))

            # get rid of empty lines
            lines = list(i for i in lines if i)

            # Rejoin the lines that you just modified
            command = '\n'.join(lines)
            launch_commands.append(command)

    return 'launch' + '\nlaunch'.join(launch_commands)

reweightCommand = ''
reweightCommand = AddParameterScan(reweightCommand,'DIM62F','ctG',[-1.0,0.0,1.0])
reweightCommand = AddParameterScan(reweightCommand,'DIM62F','ctp',[-1.0,0.0,1.0])
reweightCommand = AddParameterScan(reweightCommand,'DIM62F','cpG',[-1.0,0.0,1.0])
print('reweight command:')
print(reweightCommand)
