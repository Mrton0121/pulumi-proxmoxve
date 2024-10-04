// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.VM.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VirtualMachineWatchdogArgs extends com.pulumi.resources.ResourceArgs {

    public static final VirtualMachineWatchdogArgs Empty = new VirtualMachineWatchdogArgs();

    /**
     * The action to perform if after activation the guest fails to poll the watchdog in time  (defaults to `none`).
     * 
     */
    @Import(name="action")
    private @Nullable Output<String> action;

    /**
     * @return The action to perform if after activation the guest fails to poll the watchdog in time  (defaults to `none`).
     * 
     */
    public Optional<Output<String>> action() {
        return Optional.ofNullable(this.action);
    }

    /**
     * Whether the watchdog is enabled (defaults to `false`).
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return Whether the watchdog is enabled (defaults to `false`).
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    /**
     * The watchdog type to emulate (defaults to `i6300esb`).
     * 
     */
    @Import(name="model")
    private @Nullable Output<String> model;

    /**
     * @return The watchdog type to emulate (defaults to `i6300esb`).
     * 
     */
    public Optional<Output<String>> model() {
        return Optional.ofNullable(this.model);
    }

    private VirtualMachineWatchdogArgs() {}

    private VirtualMachineWatchdogArgs(VirtualMachineWatchdogArgs $) {
        this.action = $.action;
        this.enabled = $.enabled;
        this.model = $.model;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VirtualMachineWatchdogArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VirtualMachineWatchdogArgs $;

        public Builder() {
            $ = new VirtualMachineWatchdogArgs();
        }

        public Builder(VirtualMachineWatchdogArgs defaults) {
            $ = new VirtualMachineWatchdogArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param action The action to perform if after activation the guest fails to poll the watchdog in time  (defaults to `none`).
         * 
         * @return builder
         * 
         */
        public Builder action(@Nullable Output<String> action) {
            $.action = action;
            return this;
        }

        /**
         * @param action The action to perform if after activation the guest fails to poll the watchdog in time  (defaults to `none`).
         * 
         * @return builder
         * 
         */
        public Builder action(String action) {
            return action(Output.of(action));
        }

        /**
         * @param enabled Whether the watchdog is enabled (defaults to `false`).
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled Whether the watchdog is enabled (defaults to `false`).
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        /**
         * @param model The watchdog type to emulate (defaults to `i6300esb`).
         * 
         * @return builder
         * 
         */
        public Builder model(@Nullable Output<String> model) {
            $.model = model;
            return this;
        }

        /**
         * @param model The watchdog type to emulate (defaults to `i6300esb`).
         * 
         * @return builder
         * 
         */
        public Builder model(String model) {
            return model(Output.of(model));
        }

        public VirtualMachineWatchdogArgs build() {
            return $;
        }
    }

}
