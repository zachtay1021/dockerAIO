#!/usr/bin/python3

import docker
import sys


def main():
    target_ip = input('Target IP: ')
    try:
        client = docker.DockerClient(base_url='tcp://' + target_ip + ':2375')
        exitTrue = False
        while exitTrue is False:
            user_choice = input("Enter a command. Type 'help' to see list of commands. >> ")
            if user_choice == 'help':
                print('\n')
                print('Commands: list, stop, start, create, change, exit, help')
                print('\n')

            elif user_choice == 'list':
                print('\n')
                for container in client.containers.list(all=True):
                    print('| Name: {} | ID: {} | Status: {} |'.format(container.name, container.id, container.status))
                print('\n')

            elif user_choice == 'stop':
                print('stop container')

            elif user_choice == 'start':
                print('start container')

            elif user_choice == 'create':
                print('create container')

            elif user_choice == 'change':
                print('change target ip')

            elif user_choice == 'exit':
                sys.exit()

            else:
                print('Command not found.')

    except docker.errors.DockerException:
        print('Could not connect to target IP.')


main()
