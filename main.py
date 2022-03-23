#!/usr/bin/python3

import docker
import sys


def main():
    target_ip = input('Target IP: ')
    try:
        # client = docker.DockerClient(base_url='tcp://' + target_ip + ':2375')
        exitTrue = False
        while exitTrue is False:
            user_choice = input("Enter a command. Type 'help' to see list of commands. >> ")
            if user_choice == 'help':
                print('\n')
                print('Commands: list, stop, start, create, change, exit, help')
                print('\n')
            elif user_choice == 'list':
                container_list()
            elif user_choice == 'stop':
                container_stop()
            elif user_choice == 'start':
                container_start()
            elif user_choice == 'create':
                container_create()
            elif user_choice == 'change':
                change()
            elif user_choice == 'exit':
                sys.exit()
            else:
                print('Command not found.')

    except docker.errors.DockerException:
        print('Could not connect to target IP.')


def container_list():
    print('List all containers')


def container_stop():
    print('Stop containers')


def container_start():
    print('Start containers')


def container_create():
    print('Create containers')


def change():
    print('Change target_ip')


main()
