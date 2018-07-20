#compdef cli.py

_message_next_arg()
{
    argcount=0
    for word in "${words[@][2,-1]}"
    do
        if [[ $word != -* ]] ; then
            ((argcount++))
        fi
    done
    if [[ $argcount -le ${#myargs[@]} ]] ; then
        _message -r $myargs[$argcount]
        if [[ $myargs[$argcount] =~ ".*file.*" || $myargs[$argcount] =~ ".*path.*" ]] ; then
            _files
        fi
    fi
}

_cli.py ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'flight-director'
            )
            _values 'cli.py' $subcommands
        ;;

        (options)
            case $line[1] in
                flight-director)
                    _cli.py-flight-director
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--info)--info' \
		'(--help)--help' \
		'(--version)--version' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'about'
				'app'
				'conn-info'
				'deployment'
				'image'
				'shell'
            )
            _values 'cli.py flight director' $subcommands
        ;;

        (options)
            case $line[1] in
                about)
                    _cli.py-flight-director-about
                ;;
                app)
                    _cli.py-flight-director-app
                ;;
                conn-info)
                    _cli.py-flight-director-conn-info
                ;;
                deployment)
                    _cli.py-flight-director-deployment
                ;;
                image)
                    _cli.py-flight-director-image
                ;;
                shell)
                    _cli.py-flight-director-shell
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-about ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--json)--json' \
        
}

_cli.py-flight-director-app ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'list'
				'show'
				'update'
				'create'
				'delete'
				'list-images'
				'show-image'
            )
            _values 'cli.py flight director app' $subcommands
        ;;

        (options)
            case $line[1] in
                list)
                    _cli.py-flight-director-app-list
                ;;
                show)
                    _cli.py-flight-director-app-show
                ;;
                update)
                    _cli.py-flight-director-app-update
                ;;
                create)
                    _cli.py-flight-director-app-create
                ;;
                delete)
                    _cli.py-flight-director-app-delete
                ;;
                list-images)
                    _cli.py-flight-director-app-list-images
                ;;
                show-image)
                    _cli.py-flight-director-app-show-image
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-app-list ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--json)--json' \
        
}

_cli.py-flight-director-app-show ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<app-name>')
        _message_next_arg
    fi
}

_cli.py-flight-director-app-update ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--name=-)--name=-' \
		'(--json)--json' \

    else
        myargs=('<app-name>')
        _message_next_arg
    fi
}

_cli.py-flight-director-app-create ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<app-id>' '<app-name>')
        _message_next_arg
    fi
}

_cli.py-flight-director-app-delete ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \

    else
        myargs=('<app-id>')
        _message_next_arg
    fi
}

_cli.py-flight-director-app-list-images ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<app-name>')
        _message_next_arg
    fi
}

_cli.py-flight-director-app-show-image ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<app-name>' '<image-name>')
        _message_next_arg
    fi
}

_cli.py-flight-director-conn-info ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        
}

_cli.py-flight-director-deployment ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'lock'
				'unlock'
				'create'
				'list'
				'show'
				'log'
				'wait'
				'list-files'
            )
            _values 'cli.py flight director deployment' $subcommands
        ;;

        (options)
            case $line[1] in
                lock)
                    _cli.py-flight-director-deployment-lock
                ;;
                unlock)
                    _cli.py-flight-director-deployment-unlock
                ;;
                create)
                    _cli.py-flight-director-deployment-create
                ;;
                list)
                    _cli.py-flight-director-deployment-list
                ;;
                show)
                    _cli.py-flight-director-deployment-show
                ;;
                log)
                    _cli.py-flight-director-deployment-log
                ;;
                wait)
                    _cli.py-flight-director-deployment-wait
                ;;
                list-files)
                    _cli.py-flight-director-deployment-list-files
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-deployment-lock ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'all'
            )
            _values 'cli.py flight director deployment lock' $subcommands
        ;;

        (options)
            case $line[1] in
                all)
                    _cli.py-flight-director-deployment-lock-all
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-deployment-lock-all ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        
}

_cli.py-flight-director-deployment-unlock ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'all'
            )
            _values 'cli.py flight director deployment unlock' $subcommands
        ;;

        (options)
            case $line[1] in
                all)
                    _cli.py-flight-director-deployment-unlock-all
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-deployment-unlock-all ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        
}

_cli.py-flight-director-deployment-create ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \
		'(--deploy-type=-)--deploy-type=-' \
		'(--json)--json' \
		'(--wait)--wait' \

    else
        myargs=('<keyval>')
        _message_next_arg
    fi
}

_cli.py-flight-director-deployment-list ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--json)--json' \
        
}

_cli.py-flight-director-deployment-show ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<deployment-id>')
        _message_next_arg
    fi
}

_cli.py-flight-director-deployment-log ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<deployment-id>')
        _message_next_arg
    fi
}

_cli.py-flight-director-deployment-wait ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \

    else
        myargs=('<deployment-id>')
        _message_next_arg
    fi
}

_cli.py-flight-director-deployment-list-files ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--json)--json' \

    else
        myargs=('<deployment-id>')
        _message_next_arg
    fi
}

_cli.py-flight-director-image ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'env'
				'list'
				'create'
				'set'
				'show'
				'delete'
            )
            _values 'cli.py flight director image' $subcommands
        ;;

        (options)
            case $line[1] in
                env)
                    _cli.py-flight-director-image-env
                ;;
                list)
                    _cli.py-flight-director-image-list
                ;;
                create)
                    _cli.py-flight-director-image-create
                ;;
                set)
                    _cli.py-flight-director-image-set
                ;;
                show)
                    _cli.py-flight-director-image-show
                ;;
                delete)
                    _cli.py-flight-director-image-delete
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-image-env ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        '*::options:->options'

    case $state in
        (command)
            local -a subcommands
            subcommands=(
				'list'
				'set'
				'unset'
            )
            _values 'cli.py flight director image env' $subcommands
        ;;

        (options)
            case $line[1] in
                list)
                    _cli.py-flight-director-image-env-list
                ;;
                set)
                    _cli.py-flight-director-image-env-set
                ;;
                unset)
                    _cli.py-flight-director-image-env-unset
                ;;
            esac
        ;;
    esac

}

_cli.py-flight-director-image-env-list ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \
		'(--format=-)--format=-' \
        
}

_cli.py-flight-director-image-env-set ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \

    else
        myargs=('<keyval>' '<keyval>')
        _message_next_arg
    fi
}

_cli.py-flight-director-image-env-unset ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \

    else
        myargs=('<key>' '<key>')
        _message_next_arg
    fi
}

_cli.py-flight-director-image-list ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--json)--json' \
        
}

_cli.py-flight-director-image-create ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \

    else
        myargs=('<keyval>' '<keyval>')
        _message_next_arg
    fi
}

_cli.py-flight-director-image-set ()
{
    local context state state_descr line
    typeset -A opt_args

    if [[ $words[$CURRENT] == -* ]] ; then
        _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \

    else
        myargs=('<keyval>' '<keyval>')
        _message_next_arg
    fi
}

_cli.py-flight-director-image-show ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \
		'(--field=-)--field=-' \
		'(--json)--json' \
        
}

_cli.py-flight-director-image-delete ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
		'(--app-name=-)--app-name=-' \
		'(--image-name=-)--image-name=-' \
        
}

_cli.py-flight-director-shell ()
{
    local context state state_descr line
    typeset -A opt_args

    _arguments -C \
        ':command:->command' \
        
}


_cli.py "$@"